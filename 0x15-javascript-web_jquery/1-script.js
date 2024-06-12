const jq = document.createElement('script');
jq.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
document.head.appendChild(jq);

jq.onload = function () {
    const newColor = "#FF0000";
    $('header').css('color', newColor);
};
