$( document ).ready(function() {

    var sessionData = null;

    function doNoice(noice, status){
        var $noices = getNoices();

        //single noice
        if($noices[noice] === undefined && status){
            $noices[noice] = {};
            $noices[noice].sound = new Audio(getHost() + '/noice/mp3/' + noice + '.mp3');
            $noices[noice].sound.loop = true;
            $noices[noice].sound.play();
            $noices[noice].status = 'active';
            $noices[noice].volume = 0.5;
        } else {
            $noices[noice].sound.pause();
            $noices[noice].sound = undefined;
            $noices[noice] = undefined;
        }
        setNoices();
    }

    $('.noice').on('click', function(){
        $(this).toggleClass('active');
        doNoice($(this).next().data('noice'), $(this).hasClass('active'));
        if ($(this).hasClass('active')) {
            viewCount($(this).next().data('noice'));
        }

    });

    $( ".slider" ).slider({min:0, max:1, value:0.5, step:0.1}).on('slide', function(event){
        var noice = $(this).parents('.player').data('noice');
        var $noices = getNoices();
        $noices[noice].sound.volume = event.value;
        $noices[noice].volume = event.value;
        setNoices();
    });

    function getNoices(){

        if (!sessionData) {
            sessionData = JSON.parse(sessionStorage.getItem('noices'));
        }

        if (!sessionData) {
            sessionData = {};
        }

        return sessionData;
    }

    function setNoices(){
        sessionStorage.setItem('noices', JSON.stringify(sessionData));
    }

    doNoiceInSession();

    function doNoiceInSession(){
        $noices = getNoices();
        for(var noice in $noices){

            if ($noices[noice].status) {
                $noices[noice].sound = new Audio(getHost() + '/noice/mp3/' + noice + '.mp3');
                $noices[noice].sound.loop  = true;
                $noices[noice].sound.play();
                $noices[noice].sound.volume = $noices[noice].volume;
            }

            $('.'+noice+'-noice').addClass('active');
        }
    }

    function getHost(){
        return 'https://shkolyar.info';
    }

    function viewCount(noice) {


        $.post('/app/api/counter' , {model:'Noice:'+noice, slug:'/noice/'+noice}, function (response) {});
    }

    /** Показываем модалку звуков 1 раз месяц */
    function showModal(){
        var storage = JSON.parse(localStorage.getItem('show_noice_modal'));
        if(!storage){
            localStorage.setItem('show_noice_modal', JSON.stringify({createdAt:new Date()}));
            $('#noice-modal').modal('show');
        }
    }
    showModal();

});
