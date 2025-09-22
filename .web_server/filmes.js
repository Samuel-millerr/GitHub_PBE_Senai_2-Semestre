const films_data = {"1": {"title": "O Poderoso Chefão", "actors": "Marlon Brando, Al Pacino", "director": "Francis Coppola", "year": "1972", "genre": "Crime, Drama", "producer": "Albert S. Ruddy", "summary": "A saga da família mafiosa Corleone e seu patriarca, Vito Corleone."}, "2": {"title": "cu", "actors": "cu", "director": "cu", "year": "2000", "genre": "Romance", "producer": "cu", "summary": "cu"}};
            const length_films_data = Object.keys(films_data).length - 1;
            const cardFilm = document.getElementsByClassName("siteCardFilm");

            for(let i = 0; i <= length_films_data; i++) {
                let info_film = cardFilm[i].children;
                info_film[0].innerHTML = "Título: " + films_data[i+1]["title"];
                info_film[1].innerHTML = "Atores: " + films_data[i+1]["actors"];
                info_film[2].innerHTML = "Diretor: " + films_data[i+1]["director"];
                info_film[3].innerHTML = "Ano: " + films_data[i+1]["year"];
                info_film[4].innerHTML = "Gênero: " + films_data[i+1]["genre"];
                info_film[5].innerHTML = "Produtor: " + films_data[i+1]["producer"];
            }

            console.log(films_data);