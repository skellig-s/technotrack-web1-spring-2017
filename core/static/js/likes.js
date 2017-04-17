$(document).ready( function () {

    function updateLikes() {

        var ids = Array();

        $('.likecount').each(function () {
            ids.push($(this).data('post-id'));
        });

        $.getJSON('/blogs/posts/likes/', {ids: ids.join(',')}, function (data) {
            for (var i in data) {
                $('.likecount[data-post-id='+i+']').html(data[i]);
            }
        });
    }

    // updateLikes();

    window.setInterval(updateLikes, 2000);

    $('.likecount').click(function () {
            var url=$(this).data('likes-url');
            var element = $(this);
            $.post(url, function (data) {
                element.html(data);
            })
        }


    );

});
