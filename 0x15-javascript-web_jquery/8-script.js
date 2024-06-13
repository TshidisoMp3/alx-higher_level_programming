const jQ10 = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

jQ10.getJSON(url, function (body) {
  const name = body.name;
jQ10.each(name, function (n, names) {
    jQ10('UL#list_movies').append('<li>' + names + '</li>');
    });
});