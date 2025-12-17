#include <napi.h>

#include "rt_audio.h"


Napi::Object Init(Napi::Env env, Napi::Object exports)
{
    RtAudioWrap::Init(env, exports);

    const napi_status add_cleanup_hook_status = napi_add_env_cleanup_hook(
        env,
        [](void*)
        {
            RtAudioWrap::Destroy();
        },
        nullptr);
    NAPI_THROW_IF_FAILED_VOID(env, add_cleanup_hook_status);

    return exports;
}

NODE_API_MODULE(audify, Init)
