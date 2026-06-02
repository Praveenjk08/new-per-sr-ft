<script setup>


import { ref, onMounted, computed } from "vue";

import FeatureImages from "@/PerSquarehome/FeatureImages.vue";

import { useRoute } from "vue-router";


const route = useRoute();

const projects = ref([]);

const searchQuery = ref("");

const fetchProjects = async () => {

  try {

    // const response = await fetch(

    //   `/api/method/desirenest.api.property.get_all_project_by_status?status=${route.params.status}`

      // );
    const response = await fetch(
  `/api/method/per_sqr_ft.api.property.get_all_project_by_status?status=${route.params.status}`
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

/* Search Filter */

const filteredProjects = computed(() => {

  return projects.value.filter((project) => {

    return (

      project.project_name
        ?.toLowerCase()
        .includes(searchQuery.value.toLowerCase())

      ||

      project.full_location
        ?.toLowerCase()
        .includes(searchQuery.value.toLowerCase())

      ||

      project.status
        ?.toLowerCase()
        .includes(searchQuery.value.toLowerCase())

    );

  });

});
</script>

<template>

<section class="py-16 bg-[#f8f8f8] min-h-screen">

  <div class="max-w-7xl mx-auto px-4">

    <!-- Heading -->

    <div class="text-center mb-10">

      <h1
        class="text-4xl md:text-5xl font-bold text-[#0B1560]"
      >

        {{ route.params.status }} Projects

      </h1>

      <p class="text-gray-500 mt-3">
        Explore premium real estate properties
      </p>

    </div>

    <!-- Search Bar -->

    <div class="flex justify-center mb-14">

      <input

        v-model="searchQuery"

        type="text"

        placeholder="Search projects, location..."

        class="w-full md:w-[650px] bg-white border border-gray-200 rounded-full px-6 py-4 outline-none focus:border-[#0B1560] shadow-sm"

      />

    </div>

    <!-- Cards -->

    <div
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8"
    >

      <div

        v-for="project in filteredProjects"

        :key="project.name"

        class="bg-white rounded-3xl overflow-hidden shadow-md hover:shadow-xl transition duration-500"

      >

        <router-link
          :to="`/project/${project.name}`"
        >

          <!-- Image -->

          <div class="relative">

            <img

              :src="project.thumbnail_image"

              class="w-full h-[230px] object-cover"

            />

            <!-- Status -->

            <div
              class="absolute top-4 left-4 bg-black text-white px-4 py-2 rounded-full text-xs uppercase font-semibold"
            >
              {{ project.status }}
            </div>

          </div>

          <!-- Content -->

          <div class="p-5">

            <!-- Name -->

            <h2
              class="text-2xl font-bold text-gray-900 line-clamp-1"
            >
              {{ project.project_name }}
            </h2>

            <!-- Location -->

            <p
              class="mt-3 text-gray-500 text-sm leading-6 min-h-[48px]"
            >
              📍 {{ project.full_location || "Location Not Available" }}
            </p>

            <!-- Details -->

            <div
              class="flex flex-wrap gap-4 mt-5 text-sm text-gray-600"
            >

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

            <button
              class="mt-6 bg-[#0B1560] hover:bg-[#16248f] text-white px-5 py-3 rounded-full text-sm transition duration-300"
            >
              View Details
            </button>

          </div>

        </router-link>

      </div>

    </div>

    <!-- No Projects -->

    <div
      v-if="filteredProjects.length === 0"
      class="text-center mt-20 text-gray-500 text-lg"
    >

      No Projects Found

    </div>

  </div>

</section>

<FeatureImages/>

</template>