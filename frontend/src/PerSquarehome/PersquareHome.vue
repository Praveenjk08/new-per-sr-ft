<template>
  <!-- Hero Section -->
  <section
    class="relative h-[700px] sm:h-[700px]   overflow-hidden  mx-4  sm:mx-6 my-10  "
  >

    <!-- Background Image -->
    <img
      src="/files/real_estate_house_.jpg"
      alt="Luxury Home"
      class="w-full h-full object-cover absolute inset-0  rounded-3xl "
    />

    <!-- Content -->
    <div
      class="relative z-10 flex flex-col items-center justify-center text-center px-4 sm:px-8 py-16 sm:py-24 h-full"
    >
      <div class="max-w-5xl w-full">

        <!-- Badge -->
        <div
          class="inline-flex items-center gap-2 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full mb-6"
        >
          <span class="w-2 h-2 bg-green-500 rounded-full"></span>

          <p class="text-black text-xs sm:text-sm tracking-wide">
            Trusted Real Estate Platform
          </p>
        </div>

        <!-- Heading -->
        <h1
          class="text-white text-4xl sm:text-5xl md:text-6xl lg:text-4xl font-bold leading-tight"
        >
          Find Your Dream
          <span class="text-[#d4af37]">Property</span>
        </h1>

        <!-- Sub Heading -->
        <p
          class="text-white text-sm sm:text-xl md:text-2xl mt-6 max-w-3xl mx-auto leading-relaxed px-2"
        >
          Explore premium apartments, villas, and plots across India’s top
          locations with Per Square Feet.
        </p>

        <!-- Search Box -->
        <div
          class="mt-8 sm:mt-10 bg-white/80 backdrop-blur-xl rounded-3xl p-3 sm:p-4 shadow-xl"
        >
          <div class="flex flex-col md:flex-row gap-3">

            <!-- Input -->
            <input
              type="text"
              placeholder="Search by City, Property, Builder..."
              class="flex-1 px-4 py-3 sm:py-4 rounded-2xl outline-none bg-white text-gray-700 text-sm sm:text-lg"
            />

            <!-- Button -->
            <button
              class="bg-[#156082] hover:bg-[#0f4f68] text-white px-6 sm:px-10 py-3 sm:py-4 rounded-2xl text-sm sm:text-lg font-semibold transition-all duration-300"
            >
              Search Property
            </button>

          </div>
        </div>

        <!-- Stats -->
        <div
          class="mt-10 grid grid-cols-2 md:grid-cols-4 gap-4"
        >

          <!-- Card 1 -->
          <div
            class="bg-white/70 backdrop-blur-md rounded-2xl p-4 sm:p-5"
          >
            <h2 class="text-black text-2xl sm:text-3xl font-bold">
              500+
            </h2>

            <p class="text-gray-700 mt-1 text-sm sm:text-base">
              Projects
            </p>
          </div>

          <!-- Card 2 -->
          <div
            class="bg-white/70 backdrop-blur-md rounded-2xl p-4 sm:p-5"
          >
            <h2 class="text-black text-2xl sm:text-3xl font-bold">
              20K+
            </h2>

            <p class="text-gray-700 mt-1 text-sm sm:text-base">
              Happy Clients
            </p>
          </div>

          <!-- Card 3 -->
          <div
            class="bg-white/70 backdrop-blur-md rounded-2xl p-4 sm:p-5"
          >
            <h2 class="text-black text-2xl sm:text-3xl font-bold">
              50+
            </h2>

            <p class="text-gray-700 mt-1 text-sm sm:text-base">
              Cities
            </p>
          </div>

          <!-- Card 4 -->
          <div
            class="bg-white/70 backdrop-blur-md rounded-2xl p-4 sm:p-5"
          >
            <h2 class="text-black text-2xl sm:text-3xl font-bold">
              15+
            </h2>

            <p class="text-gray-700 mt-1 text-sm sm:text-base">
              Years Experience
            </p>
          </div>

        </div>
      </div>
    </div>
  </section>

  <PropertySlides/>

  <!-- Components -->
  <Thefamilysection />
  <!-- <Slides/> -->
  <TheKitcheniamge />
  <FeatureImages/>
  <OurServices/>
</template>

<script setup>
import FeatureImages from "./FeatureImages.vue";
import OurServices from "./OurServices.vue";
// import Slides from "./Slides.vue";
import Thefamilysection from "./Thefamilysection.vue";
import TheKitcheniamge from "./TheKitcheniamge.vue";
import PropertySlides from "./PropertySlides.vue";
</script>