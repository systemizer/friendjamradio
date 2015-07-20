curTrackIndex = 1

$(document).ready(function() {
  $('.play-track').click(function() {
    curTrackIndex = parseInt($(this).data("index"));
    generateIframe($("#playerContainer"), curTrackIndex);
  });

  generateIframe($("#playerContainer"), curTrackIndex);
});

function generateIframe(container$, trackIndex) {
  container$.empty();

  var iframe$ = $('<iframe width="100%" height="450" frameborder="0"></iframe>')
  var curTrackId = $(".play-track[data-index="+curTrackIndex+"]").data("trackid");
  iframe$.attr("src", "//w.soundcloud.com/player/?url=https://api.soundcloud.com/tracks/" + curTrackId + "&amp;hide_related=true&amp;visual=true&amp")
  container$.prepend(iframe$);

  var widget = SC.Widget(iframe$[0]);
  widget.bind(SC.Widget.Events.READY, function() { widget.play(); });
  widget.bind(SC.Widget.Events.FINISH, function() {
    curTrackIndex+=1;
    generateIframe(container$, curTrackIndex);
  });
}
