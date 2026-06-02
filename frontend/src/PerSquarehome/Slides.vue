<template>
  <!-- Building Image Slider -->
  <section
    class="relative h-[300px] overflow-hidden my-10 mx-5 sm:mx-6"
  >

    <!-- Slider Container -->
    <div
      class="relative w-full h-full overflow-hidden rounded-3xl"
    >

      <!-- Slides -->
      <div
        class="flex transition-transform duration-700 ease-in-out h-full"
        :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
      >

        <!-- Slide 1 -->
        <img
          src="../assets/images/slideiamgehome.png"
          alt="Building 1"
          class="w-full flex-shrink-0 h-full object-cover"
        />

        <!-- Slide 2 -->
        <img
          src="../assets/images/slide2home.png"
          alt="Building 2"
          class="w-full flex-shrink-0 h-full object-cover"
        />

        <!-- Slide 3 -->
        <img
          src="../assets/images/slide3home.png"
          alt="Building 3"
          class="w-full flex-shrink-0 h-full object-cover"
        />

      </div>

      <!-- Overlay -->
      <div class="absolute inset-0 bg-black/30"></div>

      <!-- Content -->
      <div
        class="absolute inset-0 flex flex-col items-center justify-center text-center px-4"
      >

        <!-- View All -->
        <div class="absolute top-6 right-6">
          <router-link
            to="/gallery"
            class="text-white underline text-sm sm:text-base hover:text-gray-200 transition"
          >
            View All
          </router-link>
        </div>

        <h1
          class="text-white text-2xl sm:text-4xl lg:text-5xl font-bold"
        >
          Find Your Dream Property
        </h1>

        <p
          class="text-white text-sm sm:text-base lg:text-lg mt-3 max-w-2xl"
        >
          Explore premium apartments, villas and luxury homes.
        </p>

      </div>

      <!-- Left Arrow -->
      <button
        @click="prevSlide"
        class="absolute left-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 text-white w-10 h-10 rounded-full"
      >
        ❮
      </button>

      <!-- Right Arrow -->
      <button
        @click="nextSlide"
        class="absolute right-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 text-white w-10 h-10 rounded-full"
      >
        ❯
      </button>

      <!-- Dots -->
      <div
        class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2"
      >
        <button
          v-for="(slide, index) in slides"
          :key="index"
          @click="currentSlide = index"
          class="w-3 h-3 rounded-full"
          :class="
            currentSlide === index
              ? 'bg-white'
              : 'bg-white/50'
          "
        ></button>
      </div>

    </div>

  </section>
</template>

<script setup>
import { ref } from "vue";

const currentSlide = ref(0);

const slides = [
  "../assets/images/slideiamgehome.png",
  "../assets/images/slide2home.png",
  "../assets/images/slide3home.png",
];

const nextSlide = () => {
  currentSlide.value =
    (currentSlide.value + 1) % slides.length;
};

const prevSlide = () => {
  currentSlide.value =
    (currentSlide.value - 1 + slides.length) % slides.length;
};
</script>