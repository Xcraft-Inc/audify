{
  "targets": [
    {
      "target_name": "audify",
      'include_dirs': [
        "<!@(node -p \"require('node-addon-api').include\")",
        "vendor/rtaudio"
      ],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      "sources": [
        "src/audify.cpp",
        "src/rt_audio_converter.cpp",
        "src/rt_audio.cpp",
        "vendor/rtaudio/RtAudio.cpp"
      ],
      "defines": ["NAPI_ENABLE_CPP_EXCEPTIONS", "NODE_ADDON_API_CPP_EXCEPTIONS"],
      "cflags": [ "-fpermissive", "-fexceptions" ],
      "cflags_cc": [ "-fpermissive", "-fexceptions" ],
    }
  ]
}