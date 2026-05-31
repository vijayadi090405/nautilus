import { useEffect, useRef } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
export default function TorpedoScene({
  diameter = 0.7,
  length = 6,
  propulsion = "Electric",
}) {

  const mountRef = useRef(null);

  useEffect(() => {

    const mount = mountRef.current;

    if (!mount) return;

    const scene = new THREE.Scene();
const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
    });

    renderer.setPixelRatio(window.devicePixelRatio);

    renderer.setSize(
      mount.clientWidth,
      mount.clientHeight
    );
    const camera = new THREE.PerspectiveCamera(
      45,
      mount.clientWidth / mount.clientHeight,
      0.1,
      1000
    );

    camera.position.set(-0.1, -0.50, 10);

    const controls =
  new OrbitControls(
    camera,
    renderer.domElement
  );

controls.enableZoom = true;
controls.enablePan = true;
controls.enableRotate = true;

controls.enableDamping = true;

controls.dampingFactor = 0.05;

    

    mount.appendChild(renderer.domElement);

    const ambientLight =
      new THREE.AmbientLight(
        0xffffff,
        1.2
      );

    scene.add(ambientLight);

    const directionalLight =
      new THREE.DirectionalLight(
        0x7dd3fc,
        2
      );

    directionalLight.position.set(
      5,
      5,
      5
    );

    scene.add(directionalLight);

    const backLight =
      new THREE.DirectionalLight(
        0xa78bfa,
        1.5
      );

    backLight.position.set(
      -5,
      3,
      -5
    );

    scene.add(backLight);

    let glowColor = 0x67e8f9;
    let bodyColor = 0x7dd3fc;

    if (propulsion === "Thermal") {
      glowColor = 0xfb923c;
      bodyColor = 0xf97316;
    }

    if (propulsion === "Pump-Jet") {
      glowColor = 0xc084fc;
      bodyColor = 0xa855f7;
    }

    const material =
      new THREE.MeshPhysicalMaterial({
        color: bodyColor,
        metalness: 0.85,
        roughness: 0.18,
        clearcoat: 1,
        clearcoatRoughness: 0.1,
      });

    const torpedoGroup =
      new THREE.Group();

    scene.add(torpedoGroup);

    const bodyGeometry =
      new THREE.CylinderGeometry(
        diameter,
        diameter,
        length,
        64
      );

    const body =
      new THREE.Mesh(
        bodyGeometry,
        material
      );

    body.rotation.z =
      Math.PI / 2;

    torpedoGroup.add(body);

    const noseGeometry =
      new THREE.ConeGeometry(
        diameter,
        diameter * 2,
        64
      );

    const nose =
      new THREE.Mesh(
        noseGeometry,
        material
      );

    nose.rotation.z =
      -Math.PI / 2;

    nose.position.x =
      -(length / 2) - diameter;

    torpedoGroup.add(nose);

    const engineGeometry =
      new THREE.CylinderGeometry(
        diameter * 0.8,
        diameter * 0.8,
        0.7,
        64
      );

    const engineMaterial =
      new THREE.MeshStandardMaterial({
        color: 0x111827,
        metalness: 1,
        roughness: 0.3,
      });

    const engine =
      new THREE.Mesh(
        engineGeometry,
        engineMaterial
      );

    engine.rotation.z =
      Math.PI / 2;

    engine.position.x =
      (length / 2) + 0.2;

    torpedoGroup.add(engine);

    const finMaterial =
      new THREE.MeshStandardMaterial({
        color: bodyColor,
        metalness: 0.7,
        roughness: 0.2,
      });

    const finGeometry =
      new THREE.BoxGeometry(
        diameter * 1.2,
        diameter * 0.08,
        diameter * 0.6
      );

    const fin1 =
      new THREE.Mesh(
        finGeometry,
        finMaterial
      );

    fin1.position.set(
      length / 2 - 1,
      diameter * 0.8,
      0
    );

    torpedoGroup.add(fin1);

    const fin2 =
      new THREE.Mesh(
        finGeometry,
        finMaterial
      );

    fin2.position.set(
      length / 2 - 1,
      -diameter * 0.8,
      0
    );

    torpedoGroup.add(fin2);

    const fin3 =
      new THREE.Mesh(
        finGeometry,
        finMaterial
      );

    fin3.rotation.z =
      Math.PI / 2;

    fin3.position.set(
      length / 2 - 1,
      0,
      diameter * 0.8
    );

    torpedoGroup.add(fin3);

    const fin4 =
      new THREE.Mesh(
        finGeometry,
        finMaterial
      );

    fin4.rotation.z =
      Math.PI / 2;

    fin4.position.set(
      length / 2 - 1,
      0,
      -diameter * 0.8
    );

    torpedoGroup.add(fin4);

    const glowGeometry =
      new THREE.SphereGeometry(
        0.25,
        32,
        32
      );

    const glowMaterial =
      new THREE.MeshBasicMaterial({
        color: glowColor,
      });

    const glow =
      new THREE.Mesh(
        glowGeometry,
        glowMaterial
      );

    glow.position.x =
      (length / 2) + 0.6;

    torpedoGroup.add(glow);

    let frameId;

    const animate = () => {

      frameId =
        requestAnimationFrame(
          animate
        );

           torpedoGroup.rotation.x += 0.002;
      torpedoGroup.rotation.y += 0.01;
      

      const pulse =
        1 +
        Math.sin(
          Date.now() * 0.005
        ) * 0.2;

      glow.scale.set(
        pulse,
        pulse,
        pulse
      );
controls.update();
      renderer.render(
        scene,
        camera
      );

    };

    animate();

    return () => {

      cancelAnimationFrame(frameId);

      renderer.dispose();

      if (
        mount &&
        renderer.domElement &&
        mount.contains(
          renderer.domElement
        )
      ) {
        mount.removeChild(
          renderer.domElement
        );
      }

    };

  }, [
    diameter,
    length,
    propulsion
  ]);

  return (
    <div
      ref={mountRef}
      className="w-full h-full"
    />
    
  );
}