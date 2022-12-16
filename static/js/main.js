document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    selectable: true,
    displayEventTime: false,
    initialDate: new Date(),
    locale: 'pt-br',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,listYear',

    },

    buttonText: {
      today:    'Hoje',
      month:    'Mês',
      week:     'Semana',
      day:      'Dia',
      list:     'Lista',
    },

    events: {
      url: 'http://127.0.0.1:8000/agenda/events',
      failure: function() {
        document.getElementById('script-warning').style.display = 'block';
      }
    },
    dateClick: function(info) {

      alert('Resource ID: ' + info.resource);
    },

    select: function(info) {
      //console.log('teste', info.event.title)

    }


  });

  calendar.render();

});




$(document).ready(function(){

    $('.datepicker').datepicker({
        language: 'pt-BR'
    });

    $( ".deleteRegister" ).click(function() {
      let url = $(this).attr("data-delete");
      $("#btnDelete").attr("href",  url);
    });

    let $select = $(".select-hours");

    for (let hr = 0; hr < 24; hr++) {
      let hrStr = hr.toString().padStart(2, "0") + ":";
      let val = hrStr + "00";
      $select.append('<option val="' + val + '">' + val + '</option>');
      val = hrStr + "30";
      $select.append('<option val="' + val + '">' + val + '</option>')
    }


});
