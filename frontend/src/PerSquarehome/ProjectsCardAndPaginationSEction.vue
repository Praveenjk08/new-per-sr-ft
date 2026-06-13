<template>
    <section class="py-5">

        <!-- Heading -->
        <div class="text-center mb-10">
            <h2 class="text-4xl font-bold">
                Explore Premium Properties
            </h2>

            <p class="text-gray-500 mt-2">
                Discover apartments, villas, plots and luxury homes
            </p>
        </div>

        <!-- Tabs -->
        <div class="flex flex-wrap justify-center gap-6 mb-6">
            <button v-for="type in propertyTypes" :key="type" @click="changeType(type)"
                class="px-5 py-2 rounded-full font-medium transition" :class="activeType === type
                    ? 'bg-orange-600 text-white'
                    : 'bg-gray-100 hover:bg-gray-200'
                    ">
                {{ type }}
            </button>
        </div>

        <!-- Cards -->
        <div v-if="paginatedProjects.length" class="mx-12   grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <!-- <div v-for="project in paginatedProjects" :key="project.name"
                class="bg-white  rounded-3xl  shadow-lg overflow-hidden hover:shadow-2xl transition">
                 -->
            <div v-for="project in paginatedProjects" :key="project.name"
                class="bg-white rounded-xl shadow-lg overflow-hidden h-[430px] flex flex-col">
                <div class="p-2 ">
                    <!-- <img :src="project.thumbnail_image" :alt="project.project_name"
                        class="w-full  rounded-lg h-64 object-cover" /> -->
                    <!-- Image -->
                    <img :src="project.thumbnail_image" :alt="project.project_name"
                        class="w-full rounded-lg h-[190px] object-cover" />
                </div>

                <div class="p-2">

                    <div class="flex justify-between items-center mb-3">
                        <span class="px-3 py-1 text-sm rounded-full bg-orange-100 text-orange-600">
                            {{ project.status }}
                        </span>
                    </div>

                    <h3 class="text-2xl font-bold mb-2">
                        {{ project.project_name }}
                    </h3>

                    <p class="text-gray-500 my-4">
                        {{ project.full_location }}
                    </p>

                    <div class="flex gap-4 text-[16px] text-gray-600 my-4">
                        <span v-if="project.bhk">
                            🏠 <span class="font-extrabold">{{ project.bhk }}</span>
                        </span>

                        <!-- <span v-if="project.bath">
                            🚿 {{ project.bath }}
                        </span>

                        <span v-if="project.floors">
                            🏢 {{ project.floors }}
                        </span> -->
                    </div>

                    <router-link :to="`/detailpage/${project.url}`" class="text-orange-600 font-medium ">
                        View Details →
                    </router-link>

                </div>
            </div>
        </div>

        <!-- No Data -->
        <div v-else class="text-center text-gray-500 py-20">
            No projects found.
        </div>

        <!-- Pagination -->
        <div v-if="totalPages > 1" class="flex justify-center items-center gap-5 mt-12">
            <button @click="prevPage" :disabled="currentPage === 1"
                class="px-5 py-2 rounded-lg bg-gray-200 disabled:opacity-50">
                Previous
            </button>

            <span class="font-semibold">
                Page {{ currentPage }} of {{ totalPages }}
            </span>

            <button @click="nextPage" :disabled="currentPage === totalPages"
                class="px-5 py-2 rounded-lg bg-orange-600 text-white disabled:opacity-50">
                Next
            </button>
        </div>

    </section>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import axios from "axios"

const projects = ref([])
const activeType = ref("Apartments")

const currentPage = ref(1)
const perPage = 6

const propertyTypes = [
    "Apartments",
    "Villas",
    "Plots",
    "Townships"
]

const getProjectsByType = async (type) => {
    try {
        const response = await axios.get(
            "/api/method/per_sqr_ft.api.property.get_projects_by_type",
            {
                params: {
                    property_type: type
                }
            }
        )

        projects.value = response.data.message || []
    } catch (error) {
        console.log(error)
    }
}

const changeType = (type) => {
    activeType.value = type
    currentPage.value = 1
    getProjectsByType(type)
}

onMounted(() => {
    getProjectsByType(activeType.value)
})

const totalPages = computed(() =>
    Math.ceil(projects.value.length / perPage)
)

const paginatedProjects = computed(() => {
    const start = (currentPage.value - 1) * perPage
    return projects.value.slice(start, start + perPage)
})

const nextPage = () => {
    if (currentPage.value < totalPages.value) {
        currentPage.value++
    }
}

const prevPage = () => {
    if (currentPage.value > 1) {
        currentPage.value--
    }
}
</script>