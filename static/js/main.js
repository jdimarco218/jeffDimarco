$(document).ready(function() {

    // AJAX GET
    $('.get-more').click(function(e){
        e.preventDefault();
        console.log('get more called...');

        $.ajax({
            "url": "/mytest/more/",
            "type": "GET",
            "dataType": "json",
            success: function(data) {
                alert('success');
            },
            error: function(data) {
                alert('error');
            },
    

        });

    });


    // AJAX POST
    $('.add-todo').click(function(){
      console.log('am i called');

        $.ajax({
            type: "POST",
            url: "/mytest/add/",
            dataType: "json",
            data: { "item": $(".todo-item").val() },
            success: function(data) {
                alert(data.message);
            }
        });

    });


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


});
