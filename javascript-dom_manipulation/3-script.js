document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');

  if (header.className === 'red') {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
});
