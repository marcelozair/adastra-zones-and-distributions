<template>
  <div class="zone-editable">
    <div
      v-if="display"
      class="zone-display"
    >
      <div>
        Zone Name: <strong>{{ name }}</strong> Distributions: {{ distributionDisplay }}
      </div>

      <button
        class="btn btn-primary"
        @click="setDisplay(false)"
        :disabled="saving"
      >
        Edit
      </button>
    </div>
    <div
      v-else
      class="zone-edit"
    >
      <div v-if="errorMessage" class="alert alert-danger" role="alert">
        {{ errorMessage }}
      </div>
      <label class="control-label">
        Zone Name
      </label>

      <input
        v-model="form.name"
        placeholder="Zone name"
        class="form-control"
        :disabled="saving"
      >

      <div class="zone-edit-distributions">
        <div :key="distribution.id" v-for="distribution in form.distributions">
          <label class="control-label">
            Distribution
          </label>

          <div class="d-flex gap-2">
            <input
              v-model="distribution.percentage"
              placeholder="Percentage"
              class="form-control"
            >
            <button
              @click="removeDistrubution(distribution.id)"
              class="btn btn-danger"
              :disabled="saving"
            >
              Remove
            </button>
          </div>
        </div>

      </div>

      <div class="zone-edit-actions">
        <button
          class="btn btn-primary"
          @click="addDistrubution()"
          :disabled="saving"
        >
          Add distribution
        </button>
        <div class="zone-actions">
          <button
            class="btn btn-secondary"
            @click="setDisplay(true)"
            :disabled="saving"
          >
          Cancel
          </button>

          <button
            class="btn btn-success"
            @click="save"
            :disabled="saving"
          >
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ZoneEditable',
  props: {
    name: String,
    id: Number,
    distributions: Array,
  },
  data() {
    return {
      errorMessage: '',
      display: true,
      form: {
        name: '',
        distributions: [],
        deletedDistributions: []
      },
      saving: false,
    };
  },
  computed: {
    distributionDisplay() {
      return this.distributions.map(distribution => `${distribution.percentage}%`).join(' - ');
    }
  },
  mounted() {
    this.getValuesFromProps();
  },
  methods: {
    getValuesFromProps() {
      this.form.name = this.name;
      this.form.distributions = this.distributions.map(distribution => {
        return {
          id: distribution.id,
          percentage: distribution.percentage
        };
      });
    },
    getDistributionId() {
      const long = this.form.distributions.length;
      if (!long) return 1;

      return this.form.distributions[long - 1].id + 1
    },
    addDistrubution() {
      this.form.distributions.push({ id: this.getDistributionId(), percentage: 0, isNew: true });
    },
    removeDistrubution(distId) {
      const deleteIndex = this.form.distributions.findIndex(({ id }) => id === distId);
      const distrubution = this.form.distributions[deleteIndex];

      if (!distrubution.isNew) this.form.deletedDistributions.push(distrubution);
      
      this.form.distributions.splice(deleteIndex, 1)
    },
    setDisplay(value) {
      this.display = value;

      if(!this.display) {
        this.getValuesFromProps();
      }
    },
    validationForm(values) {
      if (values.name.length === 0) {
        return ({ message: 'The zone name cannot be empty' });
      }

      if (values.name.includes('  ')) {
        return ({ message: 'The zone name cannot have more than one space between each word' });
      }

      let totalDistributions = 0;

      for (const distribution of values.distributions) {
        if (
          typeof distribution.percentage !== 'number' ||
          Number.isNaN(distribution.percentage)
        ) {
          return ({ message: 'Distribution percentage is invalid' });
        }

        totalDistributions += distribution.percentage;
      }

      if (totalDistributions !== 100) {
        return ({ message: 'The sum of all distributions must be ensured to be 100%' });
      }

      return false;
    },
    async save() {
      this.saving = true;

      const params = {
        id: this.id,
        name: this.form.name.trim(),
        deletedDistributions: this.form.deletedDistributions,
        distributions: this.form.distributions.map((dist) => ({
          ...dist,
          isNew: dist.isNew || false,
          percentage: !dist.percentage ? null : Number(dist.percentage)
        })),
      };

      try {
        const formErrors = this.validationForm(params);
        if (formErrors) throw new Error(formErrors.message);

        const response = await axios.put('/api/zones/edit', params);

        if (response.status === 202) {
          this.$emit('edit', {
            name: params.name,
            distributions: params.distributions
          });
        }

        this.display = true;
        if (this.errorMessage) this.errorMessage = ''; 
      } catch(error) {
        if (error.response?.data?.message) {
          this.errorMessage = error.response.data.message;
          return;
        }

        this.errorMessage = error.message;
        console.error(this.errorMessage);
      } finally {
        this.saving = false;
      }

    }
  }
}
</script>

<style lang="scss">
@import 'resources/scss/variables.scss';

.zone-editable {
  border: 1px solid $gray-color;
  padding: $qmb;
  border-radius: $border-radius;

  .zone-display {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .zone-edit {
    display: flex;
    flex-direction: column;
    gap: $small-action-space;

    .zone-edit-actions {
      display: flex;
      width: 100%;
      margin-top: $mt-btn;
      justify-content: space-between;
    }

    .zone-edit {
      display: flex;
      gap: $small-action-space;
      justify-content: end;
    }

    .zone-edit-distributions {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: $small-action-space;
    }
  }
}
</style>
