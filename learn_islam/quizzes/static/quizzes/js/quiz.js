const validTypes = [
  'choose', // {text, values: [ch1, ch2, ch3, ...]}
  'fill-in-the-blank', // {text, values: [val1, val2, val3, ...]}
  'link-the-sentences', // {title, values: [{a, b}, {a, b}, ...]}
  'choose-a-category', // {values: [{name: '', items: []}, {name: '', items: []}]}
  'true-or-false', // {text, isTrue}
];

/**
 * Default component if the user does not choose a quiz type
 */
Vue.component('no-component', {
  template: `<div>Vous devez choisir un type de quiz</div>`,
});

/**
 * Choose the correct answer quiz
 */
Vue.component('choose', {
  data() {
    if (!this.value) {
      return {
        text: '',
        values: ['', ''],
      };
    }
    return {
      text: this.value.text,
      values: this.value.values,
    };
  },
  props: ['value'],
  watch: {
    text() {
      this.$emit('input', {
        text: this.text,
        values: this.values,
      });
    },
    values() {
      this.$emit('input', {
        text: this.text,
        values: this.values,
      });
    },
  },
  template: `<div>
    <label>Texte:<br />
        <textarea
            v-model="text"
            rows="5"
            cols="33"
        />
    </label>
    <div>
        <h3>Réponses</h3>
        <div v-for="(item, index) in values">
            <label>
                {{index + 1}}:
                <input
                    type="text"
                    v-model="values[index]"
                />
            </label>
            <button
                @click="values.splice(index, 1)"
                type="button"
            >Supprimer</button>
        </div>
        <button
            @click="values.push('')"
            type="button"
        >Ajouter une réponse</button>
    </div>
  </div>`,
});

/**
 * Fill in the blank quiz (or complete the sentence)
 */
Vue.component('fill-in-the-blank', {
  data() {
    if (!this.value) {
      return {
        text: '',
        values: ['', ''],
      };
    }
    return {
      text: this.value.text,
      values: this.value.values,
    };
  },
  props: ['value'],
  watch: {
    text() {
      const text = this.text;
      const values = this.values;
      const numberOfInputs = text.split('##').length - 1;
      const length = values.length;
      if (numberOfInputs > length) {
        this.values = values.concat(
          new Array(numberOfInputs - length).fill(''),
        );
      } else if (numberOfInputs < length) {
        this.values = values.slice(0, numberOfInputs);
      }
      this.$emit('input', {
        text,
        values,
      });
    },
    values() {
      this.$emit('input', {
        text: this.text,
        values: this.values,
      });
    },
  },
  template: `<div>
    <label>Texte (insérez ## à la place des trous dans le texte):<br />
        <textarea
            v-model="text"
            rows="5"
            cols="33"
        />
    </label>
    <div>
        <h3>Réponses</h3>
        <div v-for="(item, index) in values">
            <label>
                {{index + 1}}:
                <input
                    type="text"
                    v-model="values[index]"
                />
            </label>
        </div>
    </div>
  </div>`,
});

/**
 * Link the sentence quiz
 */
Vue.component('link-the-sentences', {
  data() {
    if (!this.value) {
      return {
        title: '',
        values: [
          {
            a: '',
            b: '',
          },
          {
            a: '',
            b: '',
          },
          {
            a: '',
            b: '',
          },
        ],
      };
    }
    return {
      title: this.value.title,
      values: this.value.values,
    };
  },
  props: ['value'],
  methods: {
    change(event, index, field) {
      fieldValue = event.target.value;
      if (field == 'a') {
        this.values.splice(index, 1, {
          a: fieldValue,
          b: this.values[index].b,
        });
      } else {
        this.values.splice(index, 1, {
          a: this.values[index].a,
          b: fieldValue,
        });
      }
    },
  },
  watch: {
    title() {
      const title = this.title;
      const values = this.values;
      this.$emit('input', {
        title,
        values,
      });
    },
    values() {
      this.$emit('input', {
        title: this.title,
        values: this.values,
      });
    },
  },
  template: `<div>
    <label>Titre:<br />
        <input
            class="vTextField"
            v-model="title"
            type="text"
        />
    </label>
    <div>
        <h3>Phrases correspondantes:</h3>
        <div v-for="(item, index) in values">
            <label style="display: block;">
                Partie gauche {{index + 1}}:
                <input
                    class="vTextField"
                    type="text"
                    :value="values[index].a"
                    @input="change($event, index, 'a')"
                />
            </label>
            <label style="display: block;">
                Partie droite {{index + 1}}:
                <input
                    class="vTextField"
                    type="text"
                    :value="values[index].b"
                    @input="change($event, index, 'b')"
                />
            </label>
            <button
                @click="values.splice(index, 1)"
                type="button"
            >Supprimer</button>
        </div>
        <button
            @click="values.push({a: '', b: ''})"
            type="button"
        >Ajouter une paire</button>
    </div>
  </div>`,
});

/**
 * Choose the category quiz
 */
Vue.component('choose-a-category', {
  data() {
    console.log(this.value);
    // {values: [{name: '', items: []}, {name: '', items: []}]}
    if (!this.value) {
      return {
        values: [
          {
            name: '',
            items: '',
          },
          {
            name: '',
            items: '',
          },
        ],
      };
    }
    return {
      values: this.value.values.map(({ name, items }) => ({
        name,
        items: items.join('\n'),
      })),
    };
  },
  props: ['value'],
  methods: {
    change(event, index, field) {
      fieldValue = event.target.value;
      if (field == 'name') {
        this.values.splice(index, 1, {
          name: fieldValue,
          items: this.values[index].items,
        });
      } else {
        this.values.splice(index, 1, {
          name: this.values[index].name,
          items: fieldValue,
        });
      }
    },
  },
  watch: {
    values() {
      this.$emit('input', {
        values: this.values.map(({ name, items }) => ({
          name,
          items: items
            .split('\n')
            .map((item) => item.trim())
            .filter((item) => item !== ''),
        })),
      });
    },
  },
  template: `<div>
    <div>
        <div v-for="(item, index) in values">
            <label style="display: block;">
                Titre de la categorie
                <input
                    class="vTextField"
                    type="text"
                    :value="values[index].name"
                    @input="change($event, index, 'name')"
                />
            </label>
            <label style="display: block;">
                Partie droite {{index + 1}}:
                <textarea
                    :value="values[index].items"
                    @input="change($event, index, 'items')"
                    rows="7"
                    cols="33"
                />
            </label>
            <button
                @click="values.splice(index, 1)"
                type="button"
            >Supprimer</button>
        </div>
        <button
            @click="values.push({name: '', items: ''})"
            type="button"
        >Ajouter une categorie</button>
    </div>
  </div>`,
});

/**
 * True or false
 */
Vue.component('true-or-false', {
  data() {
    if (!this.value) {
      return {
        text: '',
        isTrue: true,
      };
    }
    return {
      text: this.value.text,
      isTrue: this.value.isTrue,
    };
  },
  props: ['value'],
  watch: {
    text() {
      this.$emit('input', {
        text: this.text,
        isTrue: this.isTrue,
      });
    },
    isTrue() {
      this.$emit('input', {
        text: this.text,
        isTrue: this.isTrue,
      });
    },
  },
  template: `<div>
      <label>Texte:<br />
          <textarea
              v-model="text"
              rows="5"
              cols="33"
          />
      </label>
      <div>
        <label>
            Le texte est vrai
            <input
                type="checkbox"
                v-model="isTrue"
            />
        </label>
      </div>
    </div>`,
});

/**
 * Quiz Wrapper
 */
Vue.component('quiz-data', {
  props: ['name', 'type', 'value'],
  data() {
    let parsedValue = null;
    try {
      //   console.log({ value: this.value });
      parsedValue = JSON.parse(this.value);
      //   console.log({ parsedValue });
    } catch (e) {
      console.log(e);
    }
    return {
      parsedValue,
    };
  },
  template: `<div>
        <component :is="dynamicComponent" v-model="parsedValue"></component>
    </div>`,
  computed: {
    dynamicComponent() {
      if (validTypes.includes(this.type)) {
        return this.type;
      }
      return 'no-component';
    },
  },
  watch: {
    parsedValue() {
      let newValue = '';
      try {
        newValue = JSON.stringify(this.parsedValue);
      } catch (e) {
        console.log('Error while transforming to json', e);
      }
      this.$emit('input', newValue);
    },
  },
});
