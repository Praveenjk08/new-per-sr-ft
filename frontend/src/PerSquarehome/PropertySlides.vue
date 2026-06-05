<script setup>
import { ref, onMounted } from "vue";

import { Swiper, SwiperSlide } from "swiper/vue";

import { Navigation, Autoplay } from "swiper/modules";

import "swiper/css";
import "swiper/css/navigation";

const projects = ref([]);

const fetchProjects = async () => {

  try {
    //api calling
    const response = await fetch(
      "/api/method/per_sqr_ft.api.property.get_all_projects"
    );

    const data = await response.json();

    projects.value = data.message;

  } catch (error) {

    console.log(error);

  }

};

onMounted(() => {
  fetchProjects();
});
</script>

<template>

  <section class="pt-2 pb-0 bg-[#f8f8f8] overflow-hidden">

    <div class="max-w-[1600px] mx-auto px-4">

      <!-- Heading -->

      <div class="relative mb-8">

        <div class="text-center">

          <h2 class="text-4xl md:text-5xl font-bold text-[#0B1560]">
            Homes For You
          </h2>

          <p class="text-gray-500 mt-3 text-base md:text-lg">
            Based on your view history
          </p>

        </div>

        <router-link to="/projects" class="
      inline-block mt-4
      md:absolute md:right-0 md:top-4
      text-[#0B1560]
      font-bold
      text-lg md:text-xl
      hover:underline
      transition-all duration-300
    ">
          View All →
        </router-link>

      </div>
      <!-- Swiper -->

      <Swiper v-if="projects.length" :modules="[Navigation, Autoplay]" :slides-per-view="4" :space-between="20"
        :loop="true" :navigation="true" :autoplay="{
          delay: 2500,
          disableOnInteraction: false
        }" :breakpoints="{
          320: {
            slidesPerView: 1,
            spaceBetween: 15
          },

          640: {
            slidesPerView: 2,
            spaceBetween: 15
          },

          1024: {
            slidesPerView: 3,
            spaceBetween: 20
          },

          1400: {
            slidesPerView: 4,
            spaceBetween: 20
          }
        }" class="project-swiper">

        <SwiperSlide v-for="project in projects" :key="project.name">

          <router-link :to="`/project/${project.url}`">

            <!-- Cards -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-2xl transition duration-500">

              <!-- Image -->

              <div class="relative overflow-hidden">

                <img :src="project.thumbnail_image" class="w-full h-[230px] p-2 rounded-[13px] object-cover" />

                <!-- Status -->

                <div
                  class="absolute top-4 left-4 bg-black text-white px-4 py-2 rounded-full text-[10px] font-semibold uppercase">
                  {{ project.status }}
                </div>

              </div>

              <!-- Content -->

              <div class="p-4">

                <!-- Project Name -->

                <h3 class="text-lg md:text-xl font-bold text-gray-900 line-clamp-1">
                  {{ project.project_name }}
                </h3>

                <!-- Location -->

                <p class="text-gray-500 mt-3 text-xl leading-6 min-h-[45px]">
                  📍 {{ project.full_location || "Location Not Available" }}
                </p>

                <!-- Details -->

                <div class="flex flex-wrap items-center gap-3 mt-4 text-gray-600 text-xl">

                  <span>
                    🛏 {{ project.bhk || "N/A" }}
                  </span>

                  <span>
                    🛁 {{ project.bath || "N/A" }}
                  </span>

                  <span>
                    📐 {{ project.super_built_up_area || "N/A" }}
                  </span>

                </div>

                <!-- Button -->

                <div class="mt-5">

                  <span class="inline-flex items-center gap-2 text-[#0B1560] font-semibold text-xl">
                    View Details →
                  </span>

                </div>

              </div>

            </div>

          </router-link>

        </SwiperSlide>

      </Swiper>

    </div>

  </section>

</template>

<style>
.project-swiper {

  padding-left: 5px;

  padding-right: 5px;

  padding-bottom: 60px;

}

/* Navigation Buttons */

.swiper-button-next,
.swiper-button-prev {

  color: #0B1560 !important;

  background: white;

  width: 42px !important;

  height: 42px !important;

  border-radius: 999px;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);

}

/* Arrow */

.swiper-button-next::after,
.swiper-button-prev::after {

  font-size: 16px !important;

  font-weight: bold;

}

/* Responsive */

@media (max-width: 768px) {

  .swiper-button-next,
  .swiper-button-prev {

    width: 35px !important;

    height: 35px !important;

  }

}
</style>