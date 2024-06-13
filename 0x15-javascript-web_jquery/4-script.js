const jQ5 = window.$;

jQ5('DIV#toggle_header').click(function () {
    jQ5('HEADER').toggleClass('green red');
    if (jQ5('HEADER').hasClass('green')) {
        jQ5('HEADER').removeClass('red');
    } else {
        jQ5('HEADER').removeClass('green');
    }
});
