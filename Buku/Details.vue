<template>
  <AppLayout title="Buku">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 leading-tight">
        Buku Details
      </h2>
    </template>
    <div class="container">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <a
            class="btn btn-primary mb-3 mt-3"
            :href="route('admin.buku.index')"
            ><font-awesome-icon icon="fa-solid fa-arrow-left"
          /></a>
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Detail Buku</h5>

              <p class="card-text">__Field__: {{ buku.__field__ }}</p>

              <a
                class="btn btn-primary mt-3"
                :href="route('admin.buku.edit', buku)"
                >Edit</a
              >
              &nbsp;
              <a class="btn btn-danger mt-3" @click="delete_item(buku)"
                >Delete</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script>
import { useForm } from "@inertiajs/vue3";
import AppLayout from "@/Layouts/AppLayout.vue";

export default {
  components: {
    AppLayout,
  },
  props: {
    buku: {
      type: Object,
    },
  },
  setup() {
    const form = useForm({});

    const delete_item = (buku) => {
      if (confirm("Are you sure you want to delete this buku?")) {
        form.delete(route("admin.buku.delete", buku.id));
      }
    };

    return {
      form,
      delete_item,
    };
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
