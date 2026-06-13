<script setup>

import FeatureImages from "@/PerSquarehome/FeatureImages.vue";
import { ref, onMounted, computed, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const projects = ref([]);

const route = useRoute();

const searchQuery = ref("");

const fetchProjects = async () => {

  try {

    const response = await fetch(
      "/api/method/per_sqr_ft.api.property.get_all_projects"
    );

    const data = await response.json();

    projects.value = data.message;

  } catch (error) {

    console.log(error);

  }

};

const getShortDescription = (html) => {
  if (!html) return "";

  const text = html.replace(/<[^>]*>/g, "");

  return text.split(" ").slice(0, 25).join(" ") + "...";
};
onMounted(() => {
  fetchProjects();
});

// watch(
//   () => route.query.search,
//   (newValue) => {
//     searchQueryFromHome.value = newValue || "";
//   }
// );

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

  <section class="py-4 bg-[#f8f8f8] min-h-screen">

    <div class="max-w-7xl mx-auto px-4">

      <!-- Heading -->

      <div class="text-center mb-10">

        <h1 class="text-4xl md:text-5xl font-bold text-[#0B1560]">
          Find Your Dream Property rams
        </h1>

        <p class="text-gray-500 mt-3">
          Explore ongoing, upcoming and completed projects
        </p>

      </div>

      <!-- Search Bar -->

      <div class="flex justify-center mb-12">

        <input v-model="searchQuery" type="text" placeholder="Search project, location or status..."
          class="w-full md:w-[700px] bg-white border border-gray-200 rounded-full px-6 py-4 outline-none focus:border-[#0B1560] shadow-sm" />

      </div>
      <!-- Projects -->
      <section class="max-w-5xl mx-auto px-4 md:px-0 pb-2 my-0">



        <div v-if="projects.length">



          <div v-for="(project, index) in filteredProjects" :key="index"
            @click="$router.push(`/detailpage/${project.url}`)"
            class="bg-white rounded-3xl shadow-sm border overflow-hidden mb-6">

            <div class="grid md:grid-cols-12">

              <!-- Image -->
              <div class="md:col-span-4 px-4 pb-4 pt-6">

                <img :src="project.thumbnail_image" :alt="project.project_name"
                  class="  rounded-lg w-full h-[220px] sm:h-[260px] md:h-[280px] object-cover" />

              </div>

              <!-- Content -->
              <div class="md:col-span-8 p-4 md:p-8 flex flex-col justify-between">

                <!-- Top -->
                <div>

                  <h2 class="text-2xl md:text-4xl font-semibold text-gray-900 mb-4">
                    {{ project.project_name }}
                  </h2>

                  <p class="text-gray-600 text-base md:text-lg leading-7 md:leading-9">
                    {{ getShortDescription(project.description) }}
                  </p>

                </div>

                <!-- Bottom -->
                <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mt-6">

                  <!-- Details -->
                  <div class="space-y-2 md:space-y-3 text-base md:text-lg">

                    <p>
                      <span class="font-semibold">
                        Location:
                      </span>
                      {{ project.full_location }}
                    </p>

                    <p>
                      <span class="font-semibold">
                        Unit Variants:
                      </span>
                      {{ project.unit_variants_lg }}
                    </p>

                    <p>
                      <span class="font-semibold">
                        Price Range:
                      </span>

                      <span class="text-cyan-600 font-semibold">
                        {{ project.bath }}
                      </span>

                    </p>

                    <p>

                      <span class="font-semibold">Status:</span>
                      <span class="pl-2 text-orange-500 font-extrabold">{{ project.status }}</span>
                    </p>

                  </div>

                  <!-- Buttons -->
                  <div class="flex flex-col sm:flex-row gap-3">

                    <router-link :to="`/detailpage/${project.url}`"
                      class="px-6 py-3 border rounded-xl text-center text-base md:text-lg hover:bg-gray-100">
                      View Project
                    </router-link>

                    <router-link :to="`/detailpage/${project.url}`" class="px-6 py-3 bg-yellow-500 text-white rounded-xl text-base md:text-lg
                                       ">

                      Get Pricing
                    </router-link>

                  </div>

                </div>

              </div>

            </div>

          </div>


        </div>



        <!-- No Data -->
        <div v-else class="text-center py-10 text-gray-500 text-xl">
          No Projects Found
        </div>


      </section>

      <!-- No Data -->
      <!-- 
      <div v-if="filteredProjects.length === 0" class="text-center mt-20 text-gray-500 text-lg">

        No Projects Found

      </div> -->

    </div>

  </section>
  <feature-images />
</template>