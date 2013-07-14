function popUpContent(content) {
    $(".shower-curtain").fadeIn();
    $(".pop-up").html("<p>test text</p>");
    $(".pop-up").fadeIn();
}

function closePopUp() {
    $(".shower-curtain").fadeOut();
    $(".pop-up").fadeOut();
}

$(".BTN-close-pop-up").click(function() {
    closePopUp();
});

$(".shower-curtain, .BTN-close-pop-up").click(function() {
    closePopUp();
});
