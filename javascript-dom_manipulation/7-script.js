fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results;
    const list = document.querySelector('#list_movies');

    for (let i = 0; i < movies.length; i++) {
      const item = document.createElement('li');
      item.textContent = movies[i].title;
      list.appendChild(item);
    }
  });
