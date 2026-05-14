import os

# -----------------------------
# Dataset paths
# -----------------------------

real_path = "extracted_frames/real"
fake_path = "extracted_frames/fake"

# -----------------------------
# Check folders exist
# -----------------------------

if not os.path.exists(real_path):
    print("REAL folder not found")
    exit()

if not os.path.exists(fake_path):
    print("FAKE folder not found")
    exit()

print("Dataset folders found successfully\n")

# -----------------------------
# Check REAL videos
# -----------------------------

real_videos = os.listdir(real_path)

print("REAL VIDEOS:")
print("-----------------------------")

for video in real_videos:

    video_folder = os.path.join(real_path, video)

    frames = os.listdir(video_folder)

    print(f"{video} -> {len(frames)} frames")

# -----------------------------
# Check FAKE videos
# -----------------------------

print("\nFAKE VIDEOS:")
print("-----------------------------")

fake_videos = os.listdir(fake_path)

for video in fake_videos:

    video_folder = os.path.join(fake_path, video)

    frames = os.listdir(video_folder)

    print(f"{video} -> {len(frames)} frames")

# -----------------------------
# Final summary
# -----------------------------

print("\n-----------------------------")
print("Dataset verification completed")
print("-----------------------------")

print(f"Total REAL videos : {len(real_videos)}")
print(f"Total FAKE videos : {len(fake_videos)}")