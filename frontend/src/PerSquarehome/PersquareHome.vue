<template>
  <!-- Hero Section -->
  <section class="relative h-[500px] sm:h-[500px]   overflow-hidden  mx-4  sm:mx-6 mb-10 mt-4 ">

    <!-- Background Image -->
    <img src="/files/real_estate_house_2.jpg" alt="Luxury Home"
      class="w-full h-full object-cover absolute inset-0  rounded-lg " />

    <!-- Content -->
    <div class="relative z-10 flex flex-col items-center justify-center text-center px-4 sm:px-8 py-16 sm:py-24 h-full">
      <div class="max-w-5xl w-full">

        <!-- Badge -->
        <div class="inline-flex items-center gap-2 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full mb-6">
          <span class="w-2 h-2 bg-green-500 rounded-full"></span>

          <p class="text-black text-xs sm:text-sm tracking-wide">
            Trusted Real Estate Platform
          </p>
        </div>

        <!-- Heading -->
        <h1 class="text-white text-4xl sm:text-5xl md:text-6xl lg:text-4xl font-bold leading-tight">
          Find Your Dream
          <span class="text-[#d4af37]">Property</span>
        </h1>

        <!-- Sub Heading -->
        <p class="text-white text-sm sm:text-xl md:text-2xl mt-6 max-w-3xl mx-auto leading-relaxed px-2">
          Explore premium apartments, villas, and plots across India’s top
          locations with Per Square Feet.
        </p>

        <!-- Search Box -->

        <!-- <div class="flex flex-col md:flex-row gap-2 mt-4">

          <input type="text" v-model="searchText" placeholder="Search by City, Property, Builder..."
            class="relative  w-full sm:w-[450px]   md:w-[440px] h-[40px] py-2 px-4 rounded-xl outline-none bg-white   text-gray-700 text-sm sm:text-lg" />

          
          <button @click="searchProperty"
            class="bg-[#156082] hover:bg-[#0f4f68] text-white px-6 sm:px-10 py-3 sm:py-4 rounded-2xl text-sm sm:text-lg font-semibold transition-all duration-300">
            Search Property
          </button>

        </div> -->


        <div class="flex flex-col md:flex-row justify-center items-center gap-2 mt-4">

          <!-- Input -->
          <input type="text" v-model="searchText" placeholder="Search by City, Property, Builder..."
            class="w-full sm:w-[450px] md:w-[440px] h-[40px] py-2 px-4 rounded-xl outline-none bg-white text-gray-700 text-sm sm:text-lg" />

          <!-- Button -->
          <button @click="searchProperty"
            class="w-full md:w-auto h-[40px] bg-[#156082] hover:bg-[#0f4f68] text-white px-6 sm:px-10 rounded-xl text-sm sm:text-lg font-semibold transition-all duration-300">
            Search Property
          </button>
        </div>
      </div>


    </div>

  </section>

  <PropertyType />

  <CompanyExprience />
  <!-- <PropertySlides /> -->

  <!-- Components -->
  <Thefamilysection />
  <!-- <Slides/> -->
  <TheKitcheniamge />
  <HomeBuyersSection />
  <BuilderLogoes />
  <OurServices />
  <FeatureImages />

</template>

<script setup>
import FeatureImages from "./FeatureImages.vue";
import OurServices from "./OurServices.vue";
// import Slides from "./Slides.vue";
import Thefamilysection from "./Thefamilysection.vue";
import TheKitcheniamge from "./TheKitcheniamge.vue";
import PropertySlides from "./PropertySlides.vue";
import { useRouter } from "vue-router";
import { ref } from "vue";
import PropertyType from "./PropertyType.vue";
import CompanyExprience from "./CompanyExprience.vue";
import HomeBuyersSection from "./HomeBuyersSection.vue";
import BuilderLogoes from "./BuilderLogoes.vue";

const router = useRouter();
const searchText = ref("");

const searchProperty = () => {
  router.push({
    path: "/search-projects",
    query: {
      search: searchText.value,
    },
  });
};


</script>