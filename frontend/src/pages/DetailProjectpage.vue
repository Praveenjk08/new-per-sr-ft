<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";

import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Pagination, Autoplay } from "swiper/modules";
import FeatureImages from "@/PerSquarehome/FeatureImages.vue";

import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";

const route = useRoute();
const router = useRouter();
// const router=userRouter();
// const router=useRoute()



const project = ref({});



const showFullDescription = ref(false);

const shortDescription = computed(() => {
  if (!project.value.description) return "";

  return project.value.description.length > 500
    ? project.value.description.slice(0, 500) + "..."
    : project.value.description;
});


const contactUs = () => {
  router.push("/contact-us");

}

const fetchProject = async () => {
  try {
    const response = await fetch(
      "/api/method/per_sqr_ft.api.property.get_all_details_from_project"
    );

    const data = await response.json();

    project.value =
      data.message.find(
        (item) => item.url === route.params.slug
      ) || {};
  } catch (error) {
    console.log(error);
  }
};



onMounted(() => {
  fetchProject();
});


</script>
<template>

  <section class="relative h-[350px] ">

    <Swiper v-if="project.carousel_images?.length" :modules="[Navigation, Pagination, Autoplay]" :slides-per-view="1"
      :loop="true" :navigation="true" :pagination="{ clickable: true }" :autoplay="{
        delay: 3500,
        disableOnInteraction: false
      }" class="h-[250px] sm:h-[350px] md:h-[350px] ">

      <SwiperSlide v-for="(item, index) in project.carousel_images" :key="index">

        <div class="relative h-[450px] sm:h-[450px] md:h-[450px] mx-auto ">

          <img :src="item.image" class="w-full h-full object-cover" />

          <div class="absolute inset-0 bg-black/55"></div>

        </div>

      </SwiperSlide>

    </Swiper>

  </section>


  <!-- ===================================== -->
  <!-- PART 2.1 : PROJECT OVERVIEW -->
  <!-- ===================================== -->

  <section class="bg-[#f5f7fb] py-10">
    <div class="bg-[#0B1560] rounded-[35px] overflow-hidden shadow-xl mx-6">

      <div class="h-2 bg-gradient-to-r from-yellow-400 to-orange-500"></div>

      <div class="p-4 text-white">

        <p class="uppercase tracking-[5px] text-sm text-yellow-300">
          Project Overview
        </p>

        <h2 class="text-4xl md:text-5xl font-bold mt-4">
          {{ project.project_name }}
        </h2>

        <div class="flex flex-wrap gap-6 mt-8 text-white/90">

          <span>📍 {{ project.full_location }}</span>
          <span>🛏 {{ project.bhk }}</span>
          <span>📐 {{ project.project_area }}</span>
          <span>🏗 {{ project.status }}</span>

        </div>

      </div>

    </div>

  </section>

  <!-- ===================================== -->
  <!-- PART 2.1 ENDS HERE -->
  <!-- ===================================== -->

  <!-- ===================================== -->
  <!-- PART 2.2 : ABOUT PROPERTY -->
  <!-- ===================================== -->

  <section class="bg-[#f5f7fb] pb-10">

    <div class="max-w-7xl mx-auto px-6">

      <div class="bg-white rounded-[35px] shadow-xl p-10">

        <p class="uppercase tracking-[5px] text-sm text-gray-400">
          About Property
        </p>

        <h3 class="text-3xl font-bold text-[#0B1560] mt-4 mb-8">
          Description
        </h3>

        <div class="text-gray-700 leading-9" v-html="showFullDescription
          ? project.description
          : shortDescription
          "></div>

        <button v-if="project.description?.length > 500" @click="showFullDescription = !showFullDescription"
          class="mt-6 text-[#0B1560] font-semibold">
          {{ showFullDescription ? "Show Less" : "Show More" }}
        </button>

      </div>

    </div>

  </section>

  <!-- ===================================== -->
  <!-- PART 2.2 ENDS HERE -->
  <!-- ===================================== -->




  <!-- ===================================== -->
  <!-- PART 2.3 : PROPERTY DETAILS -->
  <!-- ===================================== -->

  <section class="bg-[#f5f7fb] pb-16">

    <div class="max-w-7xl mx-auto px-6">

      <!-- Heading -->
      <div class="text-center mb-16">
        <p class="uppercase tracking-[6px] text-sm text-gray-400">
          Property Information
        </p>
        <h2 class="text-4xl md:text-5xl font-bold text-[#0B1560] mt-4">
          Property Details
        </h2>
      </div>

      <!-- Main Card -->
      <div class="bg-white rounded-[35px] shadow-xl overflow-hidden">

        <!-- Top Border -->
        <div class="h-2 bg-gradient-to-r from-[#0B1560] via-blue-500 to-cyan-400"></div>

        <!-- Details Grid -->
        <div class="grid md:grid-cols-2">

          <!-- Row -->
          <div class="flex justify-between items-center p-6 border-b md:border-r 
                 hover:bg-blue-50 transition duration-300 cursor-pointer">
            <span class="text-gray-500 font-medium flex items-center gap-2">
              📍 Location
            </span>
            <span class="font-semibold text-[#0B1560] text-right">
              {{ project.full_location }}
            </span>
          </div>

          <div class="flex justify-between items-center p-6 border-b 
                 hover:bg-blue-50 transition duration-300 cursor-pointer">
            <span class="text-gray-500 font-medium flex items-center gap-2">
              🏠 Bhk
            </span>
            <span class="font-semibold text-[#0B1560]">
              {{ project.bhk }}
            </span>
          </div>

          <div class="flex justify-between items-center p-6 border-b md:border-r 
                 hover:bg-blue-50 transition duration-300 cursor-pointer">
            <span class="text-gray-500 font-medium flex items-center gap-2">
              📐 Total Area
            </span>
            <span class="font-semibold text-[#0B1560]">
              {{ project.project_area }}
            </span>
          </div>

          <div class="flex justify-between items-center p-6 border-b 
                 hover:bg-blue-50 transition duration-300 cursor-pointer">
            <span class="text-gray-500 font-medium flex items-center gap-2">
              🚧 Project Status
            </span>
            <span class="font-semibold text-[#0B1560]">
              {{ project.status }}
            </span>
          </div>

          <div class="flex justify-between items-center p-6 border-b md:border-r 
                 hover:bg-blue-50 transition duration-300 cursor-pointer">
            <span class="text-gray-500 font-medium flex items-center gap-2">
              🏗️ Builder
            </span>
            <span class="font-semibold text-[#0B1560]">
              {{ project.project_by_builder }}
            </span>
          </div>

          <div class="flex justify-between items-center p-6 border-b 
                 hover:bg-blue-50 transition duration-300 cursor-pointer">
            <span class="text-gray-500 font-medium flex items-center gap-2">
              🚪 Rooms
            </span>
            <span class="font-semibold text-[#0B1560]">
              {{ project.bath }}
            </span>
          </div>

        </div>

        <!-- CTA -->
        <div class="bg-[#f8f9fc] p-8 text-center">
          <button @click="contactUs" class="bg-[#0B1560] hover:bg-[#16248f] text-white px-10 py-4 rounded-full 
                 font-semibold transition-all duration-300 hover:shadow-xl animate-pulse">
            Contact Us
          </button>
        </div>

      </div>

    </div>
  </section>

  <!-- ===================================== -->
  <!-- PART 2.3 ENDS HERE -->
  <!-- ===================================== -->



  <!-- ===================================== -->
  <!-- PART 3 : PREMIUM GALLERY SECTION -->
  <!-- ===================================== -->

  <section class="bg-[#f5f7fb] py-5">

    <div class="max-w-7xl mx-auto px-4">

      <!-- Heading -->

      <div class="text-center mb-16">

        <p class="uppercase tracking-[5px] text-sm text-gray-400">
          Project Gallery
        </p>

        <h2 class="text-4xl md:text-5xl font-bold text-[#0B1560] mt-4">
          Explore Beautiful Spaces
        </h2>

        <p class="text-gray-500 mt-4 max-w-2xl mx-auto">
          Discover every corner of this premium project through our exclusive gallery.
        </p>

      </div>

      <!-- Gallery Container -->

      <div v-if="project.gallery_images?.length" class="bg-white rounded-[30px] p-6 md:p-8 shadow-xl">

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">

          <div v-for="(item, index) in project.gallery_images.slice(0, 8)" :key="index"
            class="relative overflow-hidden rounded-xl group">

            <img :src="item.image" :alt="item.alt_text || 'Gallery Image'"
              class="w-full h-[180px] md:h-[220px] lg:h-[250px] object-cover transition duration-500 group-hover:scale-110" />

            <!-- Last Image Overlay -->

            <div v-if="
              index === 7 &&
              project.gallery_images.length > 8
            " class="absolute inset-0 bg-black/60 flex items-center justify-center">

              <span class="text-white text-4xl font-bold">
                +{{ project.gallery_images.length - 8 }}
              </span>

            </div>

          </div>

        </div>

      </div>

    </div>

  </section>

  <!-- ===================================== -->
  <!-- PART 3 ENDS HERE -->
  <!-- ===================================== -->

  <!-- ===================================== -->
  <!-- ===================================== -->
  <!-- PART 4A : PROJECT BLUEPRINT SECTION -->
  <!-- ===================================== -->

  <section v-if="project.per_square_feet_gallery?.length" class="bg-white py-5">

    <div class="max-w-7xl mx-auto px-2">

      <!-- Heading -->

      <div class="text-center mb-10">

        <p class="uppercase tracking-[5px] text-sm text-gray-400">
          Floor Plan
        </p>

        <h2 class="text-4xl md:text-5xl font-bold text-[#0B1560] mt-4">
          Project Blueprint
        </h2>

        <p class="text-gray-500 mt-6 max-w-3xl mx-auto">
          Explore detailed floor plans and layouts designed for
          maximum comfort and functionality.
        </p>

      </div>

      <!-- Blueprint Slider -->

      <div class="bg-white rounded-[35px] shadow-xl overflow-hidden">

        <Swiper :modules="[Navigation, Pagination, Autoplay]" :slides-per-view="1"
          :loop="project.per_square_feet_gallery.length > 1" :navigation="true" :pagination="{ clickable: true }"
          :autoplay="{
            delay: 3000,
            disableOnInteraction: false
          }" class="w-full">

          <SwiperSlide v-for="(item, index) in project.per_square_feet_gallery" :key="index">

            <img :src="item.image" :alt="item.alt_text" class="w-full h-[400px] object-cover bg-[#f8f9fc] p-2" />

          </SwiperSlide>

        </Swiper>

      </div>

    </div>

  </section>

  <!-- ===================================== -->
  <!-- PART 4A ENDS HERE -->
  <!-- ===================================== -->


  <!-- ===================================== -->
  <!-- PART 5 : LOCATION WITH GOOGLE MAP -->
  <!-- ===================================== -->

  <section class="bg-white py-10">

    <div class="max-w-7xl mx-auto px-4">

      <!-- Heading -->

      <div class="mb-12">

        <p class="uppercase tracking-[5px] text-sm text-gray-400">
          Location
        </p>

        <h2 class="text-4xl md:text-5xl font-bold text-[#0B1560] mt-4">
          Project Location
        </h2>

      </div>

      <!-- Map Card -->

      <div class="bg-white rounded-[35px] shadow-xl overflow-hidden">
        <iframe :src="project.project_location_map_embed"
          class="w-full h-[350px] sm:h-[350px] md:h-[450px] lg:h-[550px]" style="border:0;" loading="lazy"></iframe>

      </div>

    </div>

  </section>

  <!-- ===================================== -->
  <!-- PART 5 ENDS HERE -->
  <!-- ===================================== -->

  <!-- ===================================== -->
  <!-- PART 6 : ABOUT BUILDER -->
  <!-- ===================================== -->

  <section class="bg-[#f5f7fb] py-10">

    <div class="max-w-7xl mx-auto px-6">

      <div class="bg-white  rounded-[35px] shadow-xl overflow-hidden">

        <div class="grid lg:grid-cols-12 gap-0">

          <!-- Left Side -->

          <div class="lg:col-span-4 bg-[#0B1560] text-white p-10  flex flex-col justify-center">

            <p class="uppercase tracking-[5px] text-sm text-blue-200">
              Developer Profile
            </p>

            <h2 class="text-4xl font-bold mt-4">
              About Builder
            </h2>

          </div>

          <!-- Right Side -->

          <div class="lg:col-span-8 p-10">

            <h3 class="text-3xl font-bold text-[#0B1560] mb-6">
              {{ project.project_by_builder }}
            </h3>

            <p class="text-gray-600 leading-9 text-lg">
              {{ project.builder_description }}
            </p>

            <!-- Stats -->

            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mt-10">

              <div class="bg-[#f8f9fc] rounded-2xl p-6 text-center">

                <h4 class="text-3xl font-bold text-[#0B1560]">
                  20+
                </h4>

                <p class="text-gray-500 mt-2">
                  Years Experience
                </p>

              </div>

              <div class="bg-[#f8f9fc] rounded-2xl p-6 text-center">

                <h4 class="text-3xl font-bold text-[#0B1560]">
                  50+
                </h4>

                <p class="text-gray-500 mt-2">
                  Projects Delivered
                </p>

              </div>

              <div class="bg-[#f8f9fc] rounded-2xl p-6 text-center">

                <h4 class="text-3xl font-bold text-[#0B1560]">
                  10K+
                </h4>

                <p class="text-gray-500 mt-2">
                  Happy Families
                </p>

              </div>

              <div class="bg-[#f8f9fc] rounded-2xl p-6 text-center">

                <h4 class="text-3xl font-bold text-[#0B1560]">
                  100%
                </h4>

                <p class="text-gray-500 mt-2">
                  Trust & Quality
                </p>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>

  </section>

  <!-- ===================================== -->
  <!-- PART 6 ENDS HERE -->
  <!-- ===================================== -->

  <!-- ===================================== -->
  <!-- PART 4 : AMENITIES SECTION -->
  <!-- ===================================== -->
  <FeatureImages />
  <!-- ===================================== -->
  <!-- PART 4 ENDS HERE -->
  <!-- ===================================== -->




</template>
<style>
.swiper-button-next,
.swiper-button-prev {
  color: white !important;
}

.swiper-pagination-bullet {
  background: white !important;
}

.swiper-pagination-bullet-active {
  background: white !important;
}
</style>