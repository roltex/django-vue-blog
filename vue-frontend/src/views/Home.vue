<template>
  <div>
    <header class="hero">
      <h1>Welcome to the Blog Platform</h1>
      <p>Explore the latest blogs and stories!</p>
    </header>
    <section>
      <BlogList /> <!-- Displays the list of blogs -->
    </section>
  </div>
</template>

<script setup>
import BlogList from '../components/BlogList.vue'; // Import Blog List Component
</script>

<style>
.hero {
  text-align: center;
  background-color: #f8f9fa;
  padding: 2rem;
  margin-bottom: 1rem;
  border-bottom: 1px solid #ddd;
}

.hero h1 {
  margin: 0;
  font-size: 2.5rem;
}

.hero p {
  color: #555;
}
</style>
