<template>
  <div class="blog-list">
    <h1>Blog List</h1>
    <ul>
      <li v-for="blog in blogs" :key="blog.id" class="blog-item">
        <router-link :to="`/blog/${blog.id}`" class="blog-link">
          <h3>{{ blog.title }}</h3>
        </router-link>
        <p>{{ blog.description }}</p>
        <img v-if="blog.main_image" :src="blog.main_image" alt="Blog Image" class="blog-image"/>
        <small>By {{ blog.author }}</small>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import axios from 'axios';

const blogs = ref([]);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get('/api/blogs/');
    blogs.value = response.data;
  } catch (err) {
    console.error('Error fetching blogs:', err);
    error.value = 'Failed to load blogs. Please try again later.';
  }
});
</script>

<style>
.blog-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.blog-list h1 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: #333;
}

.blog-list ul {
  list-style: none;
  padding: 0;
}

.blog-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  background-color: #f9f9f9;
  transition: box-shadow 0.3s ease;
}

.blog-item:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.blog-link {
  text-decoration: none;
  color: #333;
}

.blog-link:hover h3 {
  text-decoration: underline;
  color: #007bff;
}

.blog-item h3 {
  font-size: 1.8rem;
  margin: 0 0 10px 0;
}

.blog-item p {
  font-size: 1rem;
  color: #555;
  margin: 0 0 10px 0;
}

.blog-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 10px 0;
}

.blog-item small {
  display: block;
  color: #888;
  font-size: 0.9rem;
}
</style>
