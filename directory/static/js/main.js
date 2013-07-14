function popUpContent(content) {
    $(".shower-curtain").fadeIn();
    $(".pop-up").html(content);
    $(".pop-up").fadeIn();
}

function showLoginForm() {
    $(".shower-curtain").fadeIn();
    $(".login-pop-up").fadeIn();
}

function closePopUp() {
    $(".shower-curtain").fadeOut();
    $(".pop-up, .login-pop-up").fadeOut();
}

$(".BTN-close-pop-up").click(function() {
    closePopUp();
});

$(".shower-curtain, .BTN-close-pop-up").click(function() {
    closePopUp();
});

$("#add-game").click(function() {
    var data = $(this).parent("form").serializeArray();
    console.log(data);
    $.post("/submitGame/", data, function(ret) {
        console.log(ret);
    });
});

$("#submit-filter select").change(function() {
    var data = $(this).parent("form").serializeArray();
    $.post("/filter/", data, function(ret) {
    
        clearMap(gameMarkers);
  
        // Configure the look of the game pins
        var pinColor = blue;
        var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34));var pinShadow = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_shadow",
        new google.maps.Size(40, 37),
        new google.maps.Point(0, 0),
        new google.maps.Point(12, 35));
        
        console.log(ret);
        
        if (ret.length > 0) {


            for (var i = 0; i < ret.length; i++) {
      
                // Build the game markers array
                gameMarkers.push(new google.maps.Marker({
                    position: new google.maps.LatLng(ret[i].lat, ret[i].long ),
                    icon: pinImage,
                    shadow: pinShadow,
                    map: map,
                    clickable: true,
                    title : i.toString()
                  })
                );
                
                gameMarkers[i].info = ret[i];
                
                // Add the click listener for that marker
                google.maps.event.addListener(gameMarkers[i], 'click', function(e) {

                    infowindow.content =   '<div id="content">'+
                            '<div class="date"></div>'+
                            '<div class="time">'+this.info.when+'</div>'+
                            '<h2 id="firstHeading" class="firstHeading">'+this.info.sport+'</h2>'+
                            '<div id="bodyContent">'+
                            '<p>'+(this.info.open ? "Open Event" : "Closed Event")+'</p>'+
                            '</div>'+
                        '</div>';
                    infowindow.open(map,this);
                });
                
              }
        } else {
           popUpContent("<p>There are no games matching your criteria. Would you like to create a new one?</p>"+
                   "<div class='actions'><a class='yesbtn' href='#' onclick='closePopUp();createGame();return false;'>Create Game</a><a class='nobtn' href='#' onclick='closePopUp();return false;'>No Thanks</a></div>"); 
        }
            
    });
});

function clearMap(overlays) {
  while(overlays[0]){
    overlays.pop().setMap(null);
  }
}

function createGame() {

    if ($("#gameCreator").length > 0) {
        if ($("#gameCreator").hasClass('opened')) {
            if ($("#gameCreator").hasClass('minimized')) {
                $("#gameCreator").removeClass('minimized');
            } else {
                $("#gameCreator").addClass('minimized');
            }
        } else {
            $("#gameCreator").addClass('opened');
        }
    } else {
        $(".shower-curtain").fadeIn();
        $(".login-pop-up").fadeIn();
    }
}

$("#id_lat, #id_long").parents("tr").each(function() {
    $(this).hide();
    $(this).prev().hide();
});
