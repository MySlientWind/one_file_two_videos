from moviepy.editor import concatenate_videoclips


def alternate_frames(clip1, clip2, fps_input=60, fps_output=120):
    # Get minimum duration to handle videos of different lengths
    min_duration = min(clip1.duration, clip2.duration)

    # Set up lists to hold the subclips
    frames1 = []
    frames2 = []

    # Extract frames
    for t in range(int(min_duration * fps_input)):
        time = t / fps_input
        if time < clip1.duration:
            frames1.append(
                clip1.to_ImageClip(time).set_duration(1 / fps_output))
        if time < clip2.duration:
            frames2.append(
                clip2.to_ImageClip(time).set_duration(1 / fps_output))

    # Create a list of alternating frames
    alternating_frames = []
    for frame1, frame2 in zip(frames1, frames2):
        alternating_frames.extend([frame1, frame2])

    # Concatenate and write to a file
    output_clip = concatenate_videoclips(alternating_frames,
                                         method="compose").set_fps(fps_output)

    return output_clip
