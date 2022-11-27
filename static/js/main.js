document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
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
      url: 'ics/feed.ics',
      format: 'ics',
      failure: function() {
        document.getElementById('script-warning').style.display = 'block';
      }
    },

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
