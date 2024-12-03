<template>
  <div class="blog-details">
    <!-- Display blog details -->
    <div v-if="blog">
      <h1>{{ blog.title }}</h1>
      <img
        v-if="blog.main_image"
        :src="blog.main_image"
        alt="Blog Image"
        class="blog-details-image"
      />
      <p>{{ blog.description }}</p>
      <small>By {{ blog.author }} on {{ formattedDate }}</small>
    </div>

    <!-- Error message if data fails to load -->
    <div v-else-if="error" class="error-message">
      {{ error }}
    </div>

    <!-- Loading message -->
    <div v-else class="loading-message">
      Loading blog details...
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute(); // Access the `id` parameter from the route
const blog = ref(null); // Blog data state
const error = ref(null); // Error message state
const formattedDate = ref(""); // For formatted blog date

// Fetch blog details on component mount
onMounted(async () => {
  try {
    const response = await axios.get(`/api/blogs/${route.params.id}/`);
    blog.value = response.data;

    // Format the date for better display
    const date = new Date(blog.value.created_at);
    formattedDate.value = date.toLocaleDateString(undefined, {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  } catch (err) {
    console.error('Error fetching blog details:', err);
    error.value = 'Failed to load blog details. Please try again later.';
  }
});
</script>

<style>
.blog-details {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.blog-details h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: #333;
}

.blog-details p {
  font-size: 1.2rem;
  color: #555;
  line-height: 1.6;
}

.blog-details small {
  display: block;
  margin-top: 20px;
  color: #888;
  font-size: 1rem;
}

.blog-details-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 20px 0;
}

.error-message {
  color: red;
  font-size: 1.2rem;
  text-align: center;
  margin-top: 50px;
}

.loading-message {
  font-size: 1.2rem;
  text-align: center;
  margin-top: 50px;
  color: #555;
}
</style>
