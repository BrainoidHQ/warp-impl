module.exports = {
	root: true,
	parser: '@typescript-eslint/parser',
	extends: ['eslint:recommended', 'plugin:@typescript-eslint/recommended', 'prettier'],
	plugins: ['svelte3', '@typescript-eslint'],
	ignorePatterns: ['*.cjs'],
	overrides: [{ files: ['*.svelte'], processor: 'svelte3/svelte3' }],
	settings: {
		'svelte3/typescript': () => require('typescript')
	},
	parserOptions: {
		sourceType: 'module',
		ecmaVersion: 2020
	},
	env: {
		browser: true,
		es2017: true,
		node: true
	},
  rules: {
    semi: ['error', 'always'],
    curly: ['error', 'multi-line', 'consistent'],
    'default-case-last': 'error',
    'dot-location': ['error', 'property'],
    'dot-notation': ['error', { allowPattern: '^[a-z]+([-_][a-z]+)+$' }],
    eqeqeq: ['error', 'always'],
    'no-alert': 'error',
    'no-constructor-return': 'error',
    'no-constant-condition': 'off',
    'no-eval': 'error',
    'no-implicit-coercion': 'error',
    'no-implicit-globals': 'warn',
    'no-invalid-this': 'error',
    'no-multi-spaces': 'error',
    'no-labels': 'warn',
    'no-lone-blocks': 'error',
    'no-loop-func': 'error',
    'no-multi-str': 'error',
    'no-new': 'error',
    'no-new-func': 'error',
    'no-new-wrappers': 'warn',
    'no-param-reassign': ['error', { props: false }],
    'no-return-assign': ['error', 'always'],
    'no-self-assign': 'error',
    'no-self-compare': 'error',
    'no-sequences': 'error',
    'no-unused-expressions': 'warn',
    'no-useless-call': 'error',
    'no-useless-catch': 'error',
    'no-useless-concat': 'error',
    'no-useless-escape': 'warn',
    'no-void': 'error',
    'no-with': 'error',
    yoda: ['error', 'never'],
    'no-undef-init': 'error',
    'no-undefined': 'error',
    'no-use-before-define': 'error',
    'array-bracket-newline': ['warn', 'consistent'],
    'array-bracket-spacing': ['error', 'never'],
    'block-spacing': ['error', 'always'],
    'brace-style': ['error', '1tbs', { allowSingleLine: true }],
    camelcase: ['warn', { properties: 'always', ignoreImports: false }],
    'comma-spacing': ['error', { before: false, after: true }],
    'comma-style': ['error', 'last'],
    'computed-property-spacing': ['error', 'never'],
    'eol-last': ['error', 'always'],
    'func-call-spacing': ['error', 'never'],
    'func-name-matching': 'warn',
    'function-call-argument-newline': ['error', 'consistent'],
    'function-paren-newline': 'off',
    'implicit-arrow-linebreak': 'off',
    indent: ['error', 2],
    'jsx-quotes': ['error', 'prefer-single'],
    'key-spacing': ['error', { beforeColon: false, afterColon: true, mode: 'strict' }],
    'keyword-spacing': ['error', { before: true, after: true }],
    'linebreak-style': ['error', 'unix'],
    'lines-between-class-members': ['error', 'never'],
    'max-len': [
      'error',
      {
        code: 180,
        ignoreTrailingComments: true,
        ignoreUrls: true,
        ignoreStrings: true,
        ignoreTemplateLiterals: true,
        ignoreRegExpLiterals: true
      },
    ],
    'multiline-ternary': ['error', 'never'],
    'new-parens': ['error', 'always'],
    'newline-per-chained-call': ['error', { ignoreChainWithDepth: 5 }],
    'no-multiple-empty-lines': ['error', { max: 3, maxEOF: 0 }],
    'no-nested-ternary': 'error',
    'no-tabs': 'error',
    'no-trailing-spaces': 'error',
    'no-whitespace-before-property': 'error',
    'nonblock-statement-body-position': 'off',
    'object-curly-newline': ['error', { multiline: true }],
    'object-curly-spacing': ['error', 'always'],
    quotes: ['error', 'single', { allowTemplateLiterals: true }],
    'semi-spacing': ['error', { before: false, after: true }],
    'sort-vars': 'error',
    'space-before-blocks': 'error',
    'space-before-function-paren': ['error', { anonymous: 'always', named: 'never', asyncArrow: 'always' }],
    'space-in-parens': ['error', 'never'],
    'arrow-body-style': ['error', 'as-needed'],
    'arrow-spacing': 'error',
    'no-var': 'error',
  }
};
