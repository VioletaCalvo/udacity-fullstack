// TODO: set a header for this file

// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
  // Remove the src so the player itself gets removed, as this is the only
  // reliable way to ensure the video stops playing in IE
  $("#trailer-video-container").empty();
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.video-play-button', function (event) {
  var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
  var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
  $("#trailer-video-container").empty().append($("<iframe></iframe>", {
    'id': 'trailer-video',
    'type': 'text-html',
    'src': sourceUrl,
    'frameborder': 0
  }));
});

// Animate in the tiles when the page loads
$(document).ready(function () {
  $('.movie-tile').hide().first().show("fast", function showNext() {
    $(this).next(".movie-tile").show("fast", showNext);
  });
});

$(document).ready(function () {
  $('.tvshow-tile').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});

// Show tooltip with video info on image hover
$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});

// Animate and offset jump scroll
// (code from stack overflow )
//   http://stackoverflow.com/questions/15158937/jquery-jump-or-scroll-to-certain-position-div-or-target-on-the-page-from-button
$(document).ready(function () {
  $('.jumper').on("click", function (event){
    event.preventDefault()
    console.log('iepa')
    theOffset = $( $(this).attr('href') ).offset()
    $("body, html").animate({
        scrollTop: theOffset.top - 70
    }, 500);
  });
});