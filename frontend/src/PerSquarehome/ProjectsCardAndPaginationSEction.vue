<template>
    <section class="pt-5 bg-[#FAF0E6]">

        <!-- Heading -->
        <div class="text-center mb-6">
            <h2 class="text-4xl font-bold">
                Explore Premium Properties
            </h2>

            <p class="text-gray-500 mt-2">
                Discover apartments, villas, plots and luxury homes
            </p>
        </div>

        <!-- Tabs -->
        <div class="mx-2 flex flex-wrap justify-center gap-6 mb-6">
            <button v-for="type in propertyTypes" :key="type" @click="changeType(type)"
                class="px-3 py-1 text-[14px] rounded-full font-medium transition" :class="activeType === type
                    ? 'bg-orange-600 text-white'
                    : 'bg-gray-100 hover:bg-gray-200'
                    ">
                {{ type }}
            </button>
        </div>



<!-- Cards -->
<div
    v-if="projects.length"
    class="mx-auto w-full px-5  md:px-8  lg:px-12">

    <Carousel
        :wrap-around="true"
        :breakpoints="breakpoints"
        :transition="500" :autoplay="4000">

        <Slide
            v-for="project in projects"
            :key="project.name">

            <div
                @click="$router.push(`/detailpage/${project.url}`)"
                class="px-2">

                <div
                    class="group bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer hover:-translate-y-1">

                    <!-- Image -->
                    <div class="relative overflow-hidden">

                        <img
                            :src="project.thumbnail_image"
                            :alt="project.project_name"
                            class="w-full h-[180px] object-cover transition duration-500 group-hover:scale-105" />

                        <!-- Status -->
                        <span
                            class="absolute top-3 left-3 bg-[#D49A37] text-white text-xs px-3 py-1 rounded-full shadow">
                            {{ project.status }}
                        </span>

                    </div>

                    <!-- Content -->
                    <div class="p-4 flex flex-col h-full">

                        <!-- Title + Price -->
                        <div class="flex justify-between items-start gap-3">

                            <h3 class="text-[14px] font-bold text-[#D49A37] line-clamp-1">
                                {{ project.project_name }}
                            </h3>

                            <div
                                class="bg-[#E8F8F0] text-[#10B981] text-[12px] font-semibold px-3 py-1 rounded-full whitespace-nowrap">

                                ₹ {{ project.price }}

                            </div>

                        </div>

                        <!-- Location -->
                        <div class="flex items-center gap-2 mt-1">

                            <span class="material-symbols-outlined text-[#D4AF37] text-[18px]">
                                location_on
                            </span>

                            <p class="text-[10px] text-gray-500  truncate w-full">
                                {{ project.full_location }}
                            </p>

                        </div>

                        <!-- Divider -->
                        <div class="border-t border-gray-200 my-2"></div>

                        <!-- Features -->
                        <div class="grid grid-cols-3 text-center pt-2">

                            <div>
                                <span class="material-symbols-outlined text-[#D49A37] text-[22px]">
                                    apartment
                                </span>

                                <p class="text-[10px] font-medium mt-1">
                                    {{ project.units }}
                                </p>
                            </div>

                            <div class="border-x border-gray-200">
                                <span class="material-symbols-outlined text-[#D49A37] text-[22px]">
                                    straighten
                                </span>

                                <p class="text-[10px] font-medium mt-1">
                                    N.A
                                </p>
                            </div>

                            <div>
                                <span class="material-symbols-outlined text-[#D49A37] text-[22px]">
                                    verified
                                </span>

                                <p class="text-[10px] font-medium mt-1">
                                    {{ project.status }}
                                </p>
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </Slide>

        <template #addons>
            <Navigation />
        </template>

    </Carousel>

</div>

        <!-- No Data -->
        <div v-else class="text-center text-gray-500 py-20">
            No projects found.
        </div>

        

    </section>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"
import { Carousel, Slide, Navigation } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const projects = ref([])
const activeType = ref("Apartments")
const router = useRouter()
const currentPage = ref(1)
const perPage = 4

const propertyTypes = [
    "Apartments",
    "Villas",
    "Plots",
    "Townships"
]

const breakpoints = {
    0: {
        itemsToShow: 1,
        snapAlign: "start",
    },
    640: {
        itemsToShow: 2,
        snapAlign: "start",
    },
    1024: {
        itemsToShow: 3,
        snapAlign: "start",
    },
    1280: {
        itemsToShow: 3.9,
        snapAlign: "start",
    },
    1536: {
        itemsToShow: 4.5,
        snapAlign: "start",
    }
}

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

<style >
/* .carousel {
    overflow: visible !important;
} */

/* .carousel__viewport {
    overflow: visible !important;
} */

.carousel__track {
    overflow: visible !important;
    padding-bottom: 20px;
}

.carousel__slide {
    padding-bottom: 20px;
}

.carousel__prev,
.carousel__next {
    position: absolute !important;
    top: 50%;
    transform: translateY(-50%);

    width: 34px !important;
    height: 34px !important;

    border-radius: 9999px !important; /* rounded-full */
    background: white !important;   /* your theme color */
    color: #fff !important;
    border: none !important;
    box-shadow: 0 8px 20px rgba(0,0,0,.2);
    z-index: 20;
}

.carousel__prev {
    left: 12px !important;
}

.carousel__next {
    right: 12px !important;
}

.carousel__icon {
    fill: black !important;
}
</style>