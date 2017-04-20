$( document ).ready(function() {

    $('.book-view').hover(
        function() {
            $(this).find('img').addClass('cover');
        }, function() {
            $(this).find('img').removeClass('cover');
        }
    );

    $('.search-button').on('click', function(e){
        $('.google-search').toggle('hide')
    });

    $('[data-submenu]').submenupicker();

    $(function () {
        $('[data-toggle="popover"]').popover()
    })
    
    $('.task').on('click', function(){
        $('.task-img').find('img').attr('src', $(this).data('img'));
        $('.task-img').find('img').attr('width', $(this).data('width'));
        $('.task-img').find('img').attr('heigth', $(this).data('heigth'));
        $('.task-number').text($(this).text());
        $('.task').filter('.active').removeClass('active');
        $(this).addClass('active');

        $('html,body').animate({
            scrollTop: $("#task-mark").offset().top
        });
    });

    $('.prev-task').on('click', function(){
        $('.task').filter('.active').prev().click()
    });

    $('.next-task').on('click', function(){
        $('.task').filter('.active').next().click()
    });
    
    // счетчик просмотра странички
    // if ($('.view-count').length) {
    //     $.post('/app/api/counter', {'model': $('.view-count').data('model'), 'slug': $('.view-count').data('slug')});
    // }

    $('.textbook-pdf').on('click', function(e){
        e.preventDefault();
        $('.pdf-embed').attr('src', $('.pdf-embed').data('pdf'));
    });

    /** top next article */
    $(document.body).on('click', '.top-next', function(e){
        e.preventDefault();

        $.post('/knowall/api/top', {page: $(this).data('page')}, function(response){
            if (response.length > 0) {
                $('.top-articles').replaceWith(response);
            } else {
                $('.top-next').hide();
            }
        });

    });
});
