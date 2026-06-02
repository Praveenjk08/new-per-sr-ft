<template>
  <div>
    <app-nav-bar />

    <router-view />

    <!-- Floating WhatsApp Button -->
    <a
      href="https://wa.me/918310673692"
      target="_blank"
      rel="noopener noreferrer"
      class="fixed bottom-20 right-5 z-50"
    >
      <img
        src="/files/WhatsApp.png"
        alt="WhatsApp"
        class="w-12 rounded-full shadow-lg hover:scale-110 transition-transform duration-300"
      />
    </a>

    <!-- Scroll To Top Button -->
    <button
      v-show="showButton"
      @click="scrollToTop"
      class="fixed bottom-5 right-5 z-50 bg-[#1f2937] hover:bg-black text-white w-12 h-12 rounded-full shadow-lg flex items-center justify-center transition-all duration-300"
    >
      <i class="bi bi-chevron-up text-2xl"></i>
    </button>

    <app-footer />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import AppNavBar from "./components/AppNavBar.vue";
import AppFooter from "./components/AppFooter.vue";

const showButton = ref(false);

const handleScroll = () => {
  showButton.value = window.scrollY > 300;
};

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onBeforeUnmount(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css";
</style>