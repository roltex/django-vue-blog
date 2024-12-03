<template>
  <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
    </ul>
  </nav>
</template>

<style>
nav ul {
  display: flex;
  gap: 1rem;
  list-style-type: none;
  padding: 0;
  margin: 0;
  background: #f8f9fa;
  border-bottom: 1px solid #ddd;
}

nav ul li {
  padding: 1rem;
}

nav ul li a {
  text-decoration: none;
  color: #007bff;
}
</style>
