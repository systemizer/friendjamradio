$(document).ready(function() {
  $('.play-track').click(function() {
    var trackId = $(this).data("trackid");
    $(".player iframe").attr("src", "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/" + trackId + "&amp;auto_play=true&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true");
  });
})
