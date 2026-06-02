<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";

/* SWIPER */

import { Swiper, SwiperSlide } from "swiper/vue";

import {
  Navigation,
  Pagination,
  Autoplay
} from "swiper/modules";

import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";



const route = useRoute();

const project = ref({});

const fetchProject = async () => {

  try {

    const response = await fetch(
      "/api/method/per_sqr_ft.api.property.get_all_details_from_project"
    );

    const data = await response.json();

    project.value = data.message.find(

      item => item.url === route.params.slug

    ) || {};

    console.log(project.value);

  } catch (error) {

    console.log(error);

  }

};

onMounted(() => {

  fetchProject();

});

watch(

  () => route.params.slug,

  () => {

    fetchProject();

  }

);
</script>

<template>

<section class="bg-[#f5f7fb] min-h-screen overflow-hidden">

  <!-- HERO SLIDER -->

  <div
    class="relative h-[500px] md:h-[850px]"
  >

    <Swiper

      v-if="project.carousel_images && project.carousel_images.length"

      :modules="[Navigation, Pagination, Autoplay]"

      :slides-per-view="1"

      :loop="project.carousel_images.length > 1"

      :navigation="true"

      :pagination="{ clickable: true }"

      :autoplay="{
        delay: 3000,
        disableOnInteraction: false
      }"

      class="w-full h-full"

    >

      <SwiperSlide

        v-for="(item, index) in project.carousel_images"

        :key="index"

      >

        <div class="relative w-full h-full">

          <!-- IMAGE -->

          <img
            :src="item.image"
            class="w-full h-full object-cover"
          />

          <!-- OVERLAY -->

          <div
            class="absolute inset-0 bg-black/45"
          ></div>

          <!-- CONTENT -->

          <div
            class="absolute bottom-16 md:bottom-24 left-1/2 -translate-x-1/2 w-full max-w-7xl px-4"
          >

            <!-- STATUS -->

            <div
              class="inline-flex items-center gap-3 bg-[#0B1560] text-white px-6 py-3 rounded-full text-sm uppercase tracking-widest mb-6 shadow-xl"
            >

              <span
                class="w-3 h-3 bg-green-400 rounded-full animate-pulse"
              ></span>

              {{ project.status }}

            </div>

            <!-- TITLE -->

            <h1
              class="text-4xl md:text-7xl font-bold text-white leading-tight max-w-5xl"
            >
              {{ project.project_name }}
            </h1>

            <!-- LOCATION -->

            <p
              class="mt-6 text-lg md:text-2xl text-gray-200"
            >
              📍 {{ project.full_location }}
            </p>

          </div>

        </div>

      </SwiperSlide>

    </Swiper>

  </div>

  <!-- MAIN -->

  <div
    class="max-w-7xl mx-auto px-4 py-20"
  >

    <!-- DESCRIPTION + DETAILS -->

    <div
      class="grid lg:grid-cols-3 gap-10"
    >

      <!-- DESCRIPTION -->

      <div
        class="lg:col-span-2"
      >

        <div
          class="bg-white rounded-[35px] shadow-xl p-8 md:p-14"
        >

          <!-- SMALL TITLE -->

          <p
            class="uppercase tracking-[5px] text-sm text-gray-400"
          >
            About Property
          </p>

          <!-- BIG TITLE -->

          <h2
            class="text-4xl md:text-5xl font-bold text-[#0B1560] mt-4 mb-10"
          >
            Luxury Living Experience
          </h2>

          <!-- DESCRIPTION -->

          <div
            class="text-gray-700 leading-10 text-lg break-words overflow-hidden max-w-full"
            v-html="project.description"
          ></div>

        </div>

      </div>

      <!-- PROPERTY DETAILS -->

      <div>

        <div
          class="bg-white rounded-[35px] shadow-xl overflow-hidden sticky top-24"
        >

          <!-- HEADING -->

          <div
            class="bg-[#0B1560] text-white px-8 py-7"
          >

            <h2
              class="text-3xl font-bold"
            >
              Property Details
            </h2>

          </div>

          <!-- TABLE -->

          <table class="w-full">

            <tbody>

              <tr class="border-b">

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  Location
                </td>

                <td class="px-6 py-5">
                  {{ project.full_location || "N/A" }}
                </td>

              </tr>

              <tr class="border-b">

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  Project Area
                </td>

                <td class="px-6 py-5">
                  {{ project.project_area || "N/A" }}
                </td>

              </tr>

              <tr class="border-b">

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  BHK
                </td>

                <td class="px-6 py-5">
                  {{ project.bhk || "N/A" }}
                </td>

              </tr>

              <tr class="border-b">

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  Bathrooms
                </td>

                <td class="px-6 py-5">
                  {{ project.bath || "N/A" }}
                </td>

              </tr>

              <tr class="border-b">

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  Floors
                </td>

                <td class="px-6 py-5">
                  {{ project.floors || "N/A" }}
                </td>

              </tr>

              <tr class="border-b">

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  Status
                </td>

                <td class="px-6 py-5">
                  {{ project.status || "N/A" }}
                </td>

              </tr>

              <tr>

                <td
                  class="bg-[#8bc4c4] text-white font-semibold px-6 py-5"
                >
                  Builder
                </td>

                <td class="px-6 py-5">
                  {{ project.project_by_builder|| "N/A" }}
                </td> 

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>

    <!-- GALLERY -->

    <div class="mt-24">

      <!-- TITLE -->

      <div
        class="text-center mb-16"
      >

        <p
          class="uppercase tracking-[5px] text-sm text-gray-400"
        >
          Property Gallery
        </p>

        <h2
          class="text-4xl md:text-5xl font-bold text-[#0B1560] mt-4"
        >
          Explore Beautiful Spaces
        </h2>

      </div>

      <!-- GALLERY IMAGES -->

      <div
        v-if="project.gallery_images && project.gallery_images.length"
        class="mb-20"
      >

        <div
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8"
        >

          <div
            v-for="(item, index) in project.gallery_images"
            :key="index"
            class="group overflow-hidden rounded-[35px] shadow-xl bg-white"
          >

            <div class="overflow-hidden">

              <img
                :src="item.image"
                class="w-full h-[320px] object-cover group-hover:scale-110 transition duration-700"
              />

            </div>

          </div>

        </div>

      </div>

      <!-- EXTRA IMAGES -->

      <div
        v-if="project.per_square_feet_gallery && project.per_square_feet_gallery.length"
      >

        <!-- HEADING -->

        <div class="mb-10">

          <h2
            class="text-4xl font-bold text-[#0B1560]"
          >
            Contact & More Images
          </h2>

        </div>

        <!-- IMAGES -->

        <div
          class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        >

          <div
            v-for="(item, index) in project.per_square_feet_gallery"
            :key="index"
            class="group overflow-hidden rounded-[35px] shadow-xl bg-white"
          >

            <div class="overflow-hidden">

              <img
                :src="item.image"
                class="w-full h-[320px] object-cover group-hover:scale-110 transition duration-700"
              />

            </div>

          </div>

        </div>

      </div>

    </div>

  </div>

</section>


</template>

<style>

.swiper {

  width: 100%;
  height: 100%;

}

.swiper-slide {

  width: 100%;
  height: 100%;

}

.swiper-button-next,
.swiper-button-prev {

  color: white !important;

  width: 55px;

  height: 55px;

  background: rgba(255,255,255,0.15);

  backdrop-filter: blur(10px);

  border-radius: 999px;

}

.swiper-button-next::after,
.swiper-button-prev::after {

  font-size: 20px;

  font-weight: bold;

}

.swiper-pagination-bullet {

  background: white !important;

  opacity: 0.7;

}

.swiper-pagination-bullet-active {

  opacity: 1;

  width: 28px;

  border-radius: 999px;

}

</style>