{
  'targets': [
    {
      'target_name': 'chromium_content',
      'type': 'shared_library',
      'dependencies': [
        'vendor/chromium/src/content/content.gyp:content',
      ], 
    },
  ],
}
