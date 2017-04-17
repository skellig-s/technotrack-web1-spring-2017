$(document).ready(

    function() {

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        $('.edit-blog-link').click(function () {
            $('#exampleModal').modal();
            $('.modal-body').load($(this).attr('href'));
            return false;
        });

        $(document).on('submit', '.ajax-form', function () {
            var form = $(this);
            $.post(form.attr('action'), form.serialize(), function (data) {
                if (data == 'OK') {
                    location.reload();
                }
                form.html(data);
            });
            return false;
        });
    }

);