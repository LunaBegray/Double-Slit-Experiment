import pygame
import numpy as np
import math
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 700
FPS = 60
PARTICLE_COUNT = 500
SLIT_WIDTH = 50
SLIT_SEPARATION = 200
WAVELENGTH = 100
DETECTOR_ACTIVE = False
HEATMAP_RESOLUTION = 5  # Controls heatmap granularity

# Colors
BACKGROUND_COLOR = (10, 10, 30)
SLIT_COLOR = (200, 200, 200)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Quantum Double-Slit Experiment with Broad Wave Interference")
clock = pygame.time.Clock()

# Heatmap array
heatmap = np.zeros((HEIGHT // HEATMAP_RESOLUTION, WIDTH // HEATMAP_RESOLUTION))

# Helper functions
def gaussian(x, mu, sigma):
    """Gaussian distribution function."""
    return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def generate_slits():
    """Generate positions of the two slits."""
    slits = []
    center_x = WIDTH // 2
    for offset in [-SLIT_SEPARATION // 2, SLIT_SEPARATION // 2]:
        for y in range(HEIGHT // 2 - SLIT_WIDTH // 2, HEIGHT // 2 + SLIT_WIDTH // 2):
            slits.append((center_x + offset, y))
    return slits

def simulate_particle():
    """Simulate a single particle trajectory and return its final position."""
    x = random.uniform(-SLIT_WIDTH // 2, SLIT_WIDTH // 2)
    slit_offset = random.choice([-SLIT_SEPARATION // 2, SLIT_SEPARATION // 2])

    if DETECTOR_ACTIVE:
        # Detector forces particle through one slit only
        x += slit_offset
    else:
        # Compute interference probability and adjust x position
        phase_difference = (2 * math.pi / WAVELENGTH) * (x - slit_offset)
        probability = 0.5 + 0.5 * math.cos(phase_difference)

        # Introduce broader spread for wave-like behavior
        if random.random() < probability:
            x += random.uniform(-WAVELENGTH, WAVELENGTH)  # Spread wave distribution
        else:
            x += random.uniform(-2 * WAVELENGTH, 2 * WAVELENGTH)  # Less probable deviations

    y = random.uniform(0, HEIGHT)  # Impact anywhere on the screen
    return WIDTH // 2 + x, y

def draw_slits(slits):
    """Draw the double slits."""
    for x, y in slits:
        pygame.draw.rect(screen, SLIT_COLOR, (x, y, 5, 2))

def simulate_wave(slits):
    """Simulate and draw interference pattern."""
    for x in range(0, WIDTH, 2):
        intensity = sum(
            gaussian(x, slit[0], WAVELENGTH // 2) for slit in slits
        )
        color_intensity = int(min(255, 255 * intensity))
        pygame.draw.line(screen, (color_intensity, color_intensity, color_intensity), (x, 0), (x, HEIGHT), 1)

def update_heatmap(particle):
    """Update the heatmap with the particle's impact position."""
    x, y = particle
    grid_x = int(x // HEATMAP_RESOLUTION)
    grid_y = int(y // HEATMAP_RESOLUTION)
    if 0 <= grid_x < heatmap.shape[1] and 0 <= grid_y < heatmap.shape[0]:
        heatmap[grid_y, grid_x] += 1

def draw_heatmap():
    """Draw the heatmap on the screen."""
    max_value = np.max(heatmap) or 1  # Avoid division by zero
    for y in range(heatmap.shape[0]):
        for x in range(heatmap.shape[1]):
            intensity = heatmap[y, x] / max_value
            color = (int(255 * intensity), int(50 * intensity), int(50 * intensity))  # Red-tinted heatmap
            rect = pygame.Rect(
                x * HEATMAP_RESOLUTION, y * HEATMAP_RESOLUTION, HEATMAP_RESOLUTION, HEATMAP_RESOLUTION
            )
            pygame.draw.rect(screen, color, rect)

# Main variables
slits = generate_slits()

# Main loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                DETECTOR_ACTIVE = not DETECTOR_ACTIVE

    # Draw the slits
    draw_slits(slits)

    # Simulate and display interference wave
    simulate_wave(slits)

    # Simulate particles
    for _ in range(10):  # Simulate multiple particles per frame for better visualization
        particle = simulate_particle()
        update_heatmap(particle)

    # Draw heatmap
    draw_heatmap()

    # Display detector status
    font = pygame.font.SysFont(None, 36)
    detector_text = f"Detector: {'ON' if DETECTOR_ACTIVE else 'OFF'}"
    detector_label = font.render(detector_text, True, (255, 255, 255))
    screen.blit(detector_label, (20, 20))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
