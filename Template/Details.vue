<template>
  <AppLayout title="__Title__">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 leading-tight">
        __Title__ Details
      </h2>
    </template>
    <div class="container">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <a
            class="btn btn-primary mb-3 mt-3"
            :href="route('admin.__table__.index')"
            ><font-awesome-icon icon="fa-solid fa-arrow-left"
          /></a>
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Detail __Title__</h5>

              <p class="card-text">__Field__: {{ __table__.__field__ }}</p>

              <a
                class="btn btn-primary mt-3"
                :href="route('admin.__table__.edit', __table__)"
                >Edit</a
              >
              &nbsp;
              <a class="btn btn-danger mt-3" @click="delete_item(__table__)"
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
    __table__: {
      type: Object,
    },
  },
  setup() {
    const form = useForm({});

    const delete_item = (__table__) => {
      if (confirm("Are you sure you want to delete this __table__?")) {
        form.delete(route("admin.__table__.delete", __table__.id));
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
