<template>
  <!-- Hero Section -->
  <!-- <section class="relative h-[500px] sm:h-[500px]   overflow-hidden  mx-4  sm:mx-6 mb-10 mt-4 "> -->
  <section class="relative h-[550px] md:h-[500px] overflow-hidden mx-2 md:mx-6 mb-10 mt-4 rounded-lg">
    <div class="absolute inset-0 bg-black/40 rounded-lg"></div>
    <!-- Background Image -->
    <!-- <img src="/files/real_estate_house_2.jpg" alt="Luxury Home"
      class="w-full h-full object-cover absolute inset-0  rounded-lg " /> -->

    <img src="/files/HomePageBannerImageNEw-One.jpeg" alt="Luxury Home"
      class="w-full h-full object-cover absolute inset-0  rounded-lg " />


    <!-- Content -->

    <div class="absolute inset-0 bg-gradient-to-b from-black/50 via-black/25 to-black/50 rounded-lg"></div>
    <!-- <div class="relative z-10 flex flex-col items-center justify-center text-center px-4 sm:px-8 py-16 sm:py-24 h-full"> -->
    <div class="relative z-10 flex flex-col items-center justify-center h-full text-center px-4 md:px-8">
      <div class="max-w-5xl w-full">

        <!-- Badge -->
        <div class="inline-flex items-center gap-2 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full my-6">
          <span class="w-2 h-2 bg-green-500 rounded-full"></span>

          <p class="text-black text-xs sm:text-sm tracking-wide">
            Trusted Real Estate Platform
          </p>
        </div>

        <!-- Heading -->
        <!-- <h1 class="text-white text-4xl sm:text-5xl md:text-6xl lg:text-4xl font-bold leading-tight"> -->
        <!-- <h1 class="text-white font-bold drop-shadow-[0_4px_12px_rgba(0,0,0,0.8)]">
          Find Your Dream
          <span class="text-[#f4b942]">
            Property
          </span>
        </h1> -->
        <!-- <div class="absolute inset-0 bg-gradient-to-b from-black/50 via-black/25 to-black/50 rounded-lg"></div> -->
        <h1
          class="text-white text-3xl sm:text-4xl md:text-7xl font-extrabold leading-tight drop-shadow-[0_4px_20px_rgba(0,0,0,0.8)]">
          Find Your Dream

          <span class="block text-[#f4b942] mt-1">
            Property
          </span>
        </h1>

        <div class="flex items-center justify-center gap-2 md:gap-4 mt-2">

          <div class="w-24 h-[2px] bg-[#f4b942]"></div>

          <!-- <span class="text-[#f4b942] text-2xl">
            🏠
          </span> -->
          <span class="material-symbols-outlined text-[#f4b942] text-[50px]">
            real_estate_agent
          </span>

          <div class="w-24 h-[2px] bg-[#f4b942]"></div>
          <!-- <div class="w-12 md:w-24 h-[2px] bg-[#f4b942]"></div> -->
        </div>


        <!-- Sub Heading -->
        <!-- <p class="text-white text-sm sm:text-xl md:text-2xl mt-6 max-w-3xl mx-auto leading-relaxed px-2">
          Explore premium apartments, villas, and plots across India’s top
          locations with Per Square Feet.
        </p> -->
        <p
          class="text-white text-sm sm:text-base md:text-2xl mt-4 max-w-4xl mx-auto leading-relaxed px-4 drop-shadow-lg">
          Explore premium apartments, villas and plots across
          India's top locations with

          <span class="text-[#f4b942] font-semibold">
            Per Square Feet
          </span>
        </p>



        <!-- <div class="flex flex-col md:flex-row justify-center items-center gap-2 mt-4">

          Input
          <input type="text" v-model="searchText" placeholder="Search by City, Property, Builder..."
            class="w-full sm:w-[450px] md:w-[440px] h-[40px] py-2 px-4 rounded-xl outline-none bg-white text-gray-700 text-sm sm:text-lg" />

          Button
          <button @click="searchProperty"
            class="w-full md:w-auto h-[40px] bg-[#156082] hover:bg-[#0f4f68] text-white px-6 sm:px-10 rounded-xl text-sm sm:text-lg font-semibold transition-all duration-300">
            Search Property
          </button>
        </div> -->
        <div class="flex flex-col md:flex-row justify-center items-start gap-2 mt-4 px-4">
          <div class="relative w-full md:w-[440px]"> <input type="text" v-model="searchText1" @input="searchProjects"
              placeholder="Search by City, Property, Builder..."
              class="w-full h-[40px] py-2 px-4 rounded-xl outline-none bg-white text-gray-700 text-sm sm:text-lg" />
            <div v-if="suggestions.length"
              class="absolute top-full left-0 w-full bg-white rounded-xl shadow-xl mt-1 z-50 max-h-80 overflow-y-auto">
              <div v-for="project in suggestions" :key="project.url" @click="selectProject(project)"
                class="px-4 py-3 hover:bg-gray-100 cursor-pointer border-b">
                <div class="font-semibold text-gray-800">
                  {{ project.project_name }}
                </div>

                <div class="text-sm text-gray-500">
                  📍 {{ project.full_location }}
                </div>
              </div>
            </div>
          </div> <button @click="searchProperty"
            class="w-full md:w-auto h-[40px] bg-[#156082] hover:bg-[#0f4f68] text-white px-6 sm:px-10 rounded-xl text-sm sm:text-lg font-semibold">
            Search Property </button>
        </div>




      </div>
      <div class="grid grid-cols-3 gap-2 md:gap-8 mt-8 md:mt-10 text-white w-full max-w-3xl">

        <!-- Projects -->
        <div class="flex flex-col items-center">

          <div class="w-16 h-16 rounded-full bg-[#0B4F6C] flex items-center justify-center">
            <span class="material-symbols-outlined text-[#f4b942] text-[40px]">
              apartment
            </span>
          </div>

          <div class="text-center">
            <h3 class="text-4xl font-bold">500+</h3>
            <p class="text-lg">Projects</p>
          </div>

        </div>

        <!-- Builders -->
        <div class="flex flex-col items-center">

          <div class="w-16 h-16 rounded-full bg-[#0B4F6C] flex items-center justify-center">
            <span class="material-symbols-outlined text-[#f4b942] text-[40px]">
              groups
            </span>
          </div>

          <div class="text-center">
            <h3 class="text-4xl font-bold">50+</h3>
            <p class="text-lg">Builders</p>
          </div>

        </div>

        <!-- Happy Buyers -->
        <div class="flex flex-col items-center">

          <div class="w-16 h-16 rounded-full bg-[#0B4F6C] flex items-center justify-center">
            <span class="material-symbols-outlined text-[#f4b942] text-[40px]">
              person
            </span>
          </div>

          <div class="text-center">
            <h3 class="text-4xl font-bold">20K+</h3>
            <p class="text-lg">Happy Buyers</p>
          </div>

        </div>

      </div>
    </div>


  </section>

  <PropertyType />
  <ProjectsCardAndPaginationSEction />

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
  <Cta />

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
import ProjectsCardAndPaginationSEction from "./ProjectsCardAndPaginationSEction.vue";
import axios from "axios";
import Cta from "./Cta.vue";


const router = useRouter();
const searchText = ref("");

const searchProperty = () => {
  router.push({
    path: "/projects",
    query: {
      search: searchText.value,
    },
  });
};

const searchText1 = ref("")
const suggestions = ref([])

const searchProjects = async () => {
  if (!searchText1.value.trim()) {
    suggestions.value = []
    return
  }


  const response = await axios.get("/api/method/per_sqr_ft.api.property.get_details_by_serch",
    {
      params: {
        search: searchText1.value
      }
    }
  )

  suggestions.value = response.data.message || []
}

const selectProject = (project) => {
  searchText1.value = project.project_name
  searchText1.value = project.full_location

  suggestions.value = []

  router.push(`/detailpage/${project.url}`)
}
</script>