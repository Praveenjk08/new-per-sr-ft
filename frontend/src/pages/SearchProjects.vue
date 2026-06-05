<template>

  <section class="py-16 bg-[#f8f8f8] min-h-screen">

    <div class="max-w-7xl mx-auto px-4">

      <!-- Heading -->

      <div class="text-center mb-10">

        <h1 class="text-4xl md:text-5xl font-bold text-[#0B1560]">
          Find Your Dream Property
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

      <!-- Projects Grid -->

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">

        <div v-for="project in filteredProjects" :key="project.name"
          class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-2xl transition duration-500">

          <router-link :to="`/project/${project.url}`">

            <!-- Image -->

            <div class="relative">

              <img :src="project.thumbnail_image" class="w-full h-[240px] p-2 object-cover rounded-[13px]" />

              <!-- Status -->

              <div
                class="absolute top-4 left-4 bg-black text-white px-4 py-2 rounded-full text-xs uppercase font-semibold">

                {{ project.status }}

              </div>

            </div>

            <!-- Content -->

            <div class="p-5">

              <!-- Name -->

              <h2 class="text-xl font-bold text-gray-900 line-clamp-1">
                {{ project.project_name }}
              </h2>

              <!-- Location -->

              <p class="mt-3 text-gray-500 text-sm leading-6 min-h-[50px]">
                📍 {{ project.full_location || "Location Not Available" }}
              </p>

              <!-- Details -->

              <div class="flex flex-wrap gap-4 mt-4 text-sm text-gray-600">

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
                class="mt-6 bg-black text-white px-5 py-3 rounded-full text-sm font-medium hover:bg-[#0B1560] transition">
                Know More
              </button>

            </div>

          </router-link>

        </div>

      </div>

      <!-- No Data -->

      <div v-if="filteredProjects.length === 0" class="text-center mt-20 text-gray-500 text-lg">

        No Projects Found

      </div>

    </div>

  </section>
  <feature-images />


</template>
<script setup>
import FeatureImages from "@/PerSquarehome/FeatureImages.vue";
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

const projects = ref([]);

// Search text from Home page URL
const homeSearch = route.query.search || "";

// Search box on Search Page
const searchQuery = ref("");

const fetchProjects = async () => {
  try {
    const response = await fetch(
      "/api/method/per_sqr_ft.api.property.get_all_projects"
    );

    const data = await response.json();

    projects.value = data.message || [];
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  fetchProjects();
});

const filteredProjects = computed(() => {
  // If user types in search page use that
  // otherwise use Home page search
  const search = (
    searchQuery.value || homeSearch
  ).toLowerCase();

  if (!search) {
    return projects.value;
  }

  return projects.value.filter((project) => {
    return (
      project.project_name
        ?.toLowerCase()
        .includes(search) ||

      project.full_location
        ?.toLowerCase()
        .includes(search) ||

      project.status
        ?.toLowerCase()
        .includes(search)
    );
  });
});
</script>

<!-- <script setup>
import FeatureImages from "@/PerSquarehome/FeatureImages.vue";
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

const projects = ref([]);

// Get search text from Home page URL
const searchQuery = ref(route.query.search || "");

const fetchProjects = async () => {
  try {
    const response = await fetch(
      "/api/method/per_sqr_ft.api.property.get_all_projects"
    );

    const data = await response.json();

    projects.value = data.message || [];
  } catch (error) {
    console.log(error);
  }
};

onMounted(() => {
  fetchProjects();
});

// Filter Projects
const filteredProjects = computed(() => {
  const search = searchQuery.value.toLowerCase();

  if (!search) return projects.value;

  return projects.value.filter((project) => {
    return (
      project.project_name?.toLowerCase().includes(search) ||
      project.full_location?.toLowerCase().includes(search) ||
      project.status?.toLowerCase().includes(search)
    );
  });
});


</script> -->