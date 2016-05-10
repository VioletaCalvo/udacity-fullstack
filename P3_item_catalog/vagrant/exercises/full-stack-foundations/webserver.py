from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi # Common Gateway Interface

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# HANDLER Class
class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<a href='/create'>New Restaurant</a>"
                output += "<h1>List of restaurants</h1>"
                for restaurant in session.query(Restaurant).all():
                    output += '''
                            <p>%s</p>
                            <a href='/%s/edit'>Edit</a>
                            <a href='/%s/delete'>Delete</a>
                            <br><br><br>
                        ''' % (restaurant.name, restaurant.id, restaurant.id)
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                # get restaurant id from path
                restaurantId = self.path[1:-5]
                # find restaurant in DB
                restaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
                output += "<h1>Edit restaurant: %s</h1>" % restaurant.name
                output += '''
                    <form method='POST' enctype='multipart/form-data' action='/%s/edit'><h2>Restaurant name</h2><input name="message" type="text"><input type="submit" value="Edit"> </form>
                    ''' % restaurant.id
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/delete"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                # get restaurant id from path
                restaurantId = self.path[1:-7]
                # find restaurant in DB
                restaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
                output += "<h1>Delete restaurant: %s</h1>" % restaurant.name
                output += '''
                    <form method='POST' enctype='multipart/form-data' action='/%s/delete'><h2>Please, confirm that you want to delete this restaurant</h2><input type="submit" value="Delete"> </form>
                    ''' % restaurant.id
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/create"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Create restaurant</h1>"
                output += '''
                    <form method='POST' enctype='multipart/form-data' action='/create'><h2>Restaurant name</h2><input name="message" type="text"><input type="submit" value="Create"> </form>
                    '''
                output += "</body></html>"
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            
            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
 
            if self.path.endswith('/create'):
                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                outputMessage = "Restaurant %s created sucessfully!" % messagecontent[0]
            elif self.path.endswith('/edit'):
                restaurantId = self.path[1:-5]
                restaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
                restaurant.name = messagecontent[0]
                session.add(restaurant)
                outputMessage = "Restaurant (%s) %s edited sucessfully!" % (restaurantId, restaurant.name)
            elif self.path.endswith('/delete'):
                restaurantId = self.path[1:-7]
                restaurant = session.query(Restaurant).filter_by(id = restaurantId).one()
                session.delete(restaurant)
                outputMessage = "Restaurant (%s) %s deleted sucessfully!" % (restaurantId, restaurant.name)

            session.commit()

            output = ""
            output += "<html><body>"
            output += "<h2> POST resutl: </h2>"
            output += "<h3> %s </h3>" % outputMessage
            output += "<a href='/restaurants'>List of restaurants</a>"
            output += "</body></html>"
            self.wfile.write(output)

        except:
            print "POST error"
            pass

# MAIN method
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()



if __name__ == '__main__':
    main()