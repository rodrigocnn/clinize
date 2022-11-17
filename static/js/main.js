$(document).ready(function(){

    $('.datepicker').datepicker({
        language: 'pt-BR'
    });

    $( ".deleteRegister" ).click(function() {
      let url = $(this).attr("data-delete");
      $("#btnDelete").attr("href",  url);
    });

});
