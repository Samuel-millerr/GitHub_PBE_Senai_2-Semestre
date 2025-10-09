<template>
    <header id="site-header">
        <router-link to="/" id="header-logo"> Biblioteca </router-link>

        <div id="links-conteiner">
          <router-link to="/authors" class="header-link" active-class="header-link-active"> Autores </router-link>
          <router-link to="/publishers" class="header-link" active-class="header-link-active"> Editoras </router-link>
          <router-link to="/books" class="header-link" active-class="header-link-active"> Livros </router-link>
        </div>
    </header> 
</template>

<style scoped>
#site-header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  background-color: #2c3e50;
  color: white;
  padding: 2rem 2rem 2rem 3rem;
}

#links-conteiner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.header-link {
  display: flex;
  align-items: center;
  text-align: center;
  max-height: 2.5rem;
  padding: 0.5rem 1rem 0.5rem 1rem;
  font-size: 24px;
  font-weight: 500;
  border: none;
  background-color: transparent;
  color: white;
  transition: 1s;
  cursor: pointer;
  text-decoration: none;
  border-radius: 4px;
}

.header-link-active {
  background-color: #65b2ff7c;
}

.header-link:hover  {
  transform: translateY(-4px);
}

#header-logo {
  font-size: 38px;
  cursor: pointer;
  color: white;
  text-decoration: none;
}
</style>
