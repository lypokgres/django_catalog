
    $("#search__form").on("submit", function () {
        $.ajax({
            url: '/search_ajax/',
            type: 'post',
            data: {
                query: $("#search__input").val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            dataType: 'json',
            success: [
                function (data) {
                    $('.good').html(data['search_ajax'])
                }
            ],
            error: [
                function () {
                    alert('Oops!')
                }
            ]
        })
        return false
    });

    var $buttons = $(".category__button");

    $buttons.on('click', function () {
        var $this = $(this)
        if ($this.next().hasClass('first')) {
            $('.category__list').not($this.next()).removeClass('show')
            $buttons.not($this).removeClass('active')
        }
        $this.toggleClass('active')
        $this.next().toggleClass('show')
    })
