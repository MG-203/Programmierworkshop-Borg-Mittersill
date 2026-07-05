import numpy as np


WRIST = 0
THUMB_CMC = 1
THUMB_MCP = 2
THUMB_IP = 3
THUMB_TIP = 4
INDEX_FINGER_MCP = 5
INDEX_FINGER_PIP = 6
INDEX_FINGER_DIP = 7
INDEX_FINGER_TIP = 8
MIDDLE_FINGER_MCP = 9
MIDDLE_FINGER_PIP = 10
MIDDLE_FINGER_DIP = 11
MIDDLE_FINGER_TIP = 12
RING_FINGER_MCP = 13
RING_FINGER_PIP = 14
RING_FINGER_DIP = 15
RING_FINGER_TIP = 16
PINKY_MCP = 17
PINKY_PIP = 18
PINKY_DIP = 19
PINKY_TIP = 20

def isFist(hand_landmarks):
    index_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    index_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    middle_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    middle_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    ring_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    ring_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    pinky_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_TIP].z - hand_landmarks[WRIST].z]))
    pinky_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_PIP].z - hand_landmarks[WRIST].z]))

    index_tip_index_mcp_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_TIP].x - hand_landmarks[INDEX_FINGER_MCP].x, hand_landmarks[INDEX_FINGER_TIP].y - hand_landmarks[INDEX_FINGER_MCP].y, hand_landmarks[INDEX_FINGER_TIP].z - hand_landmarks[INDEX_FINGER_MCP].z]))
    index_pip_index_mcp_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_PIP].x - hand_landmarks[INDEX_FINGER_MCP].x, hand_landmarks[INDEX_FINGER_PIP].y - hand_landmarks[INDEX_FINGER_MCP].y, hand_landmarks[INDEX_FINGER_PIP].z - hand_landmarks[INDEX_FINGER_MCP].z]))
    middle_tip_middle_mcp_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_TIP].x - hand_landmarks[MIDDLE_FINGER_MCP].x, hand_landmarks[MIDDLE_FINGER_TIP].y - hand_landmarks[MIDDLE_FINGER_MCP].y, hand_landmarks[MIDDLE_FINGER_TIP].z - hand_landmarks[MIDDLE_FINGER_MCP].z]))
    middle_pip_middle_mcp_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_PIP].x - hand_landmarks[MIDDLE_FINGER_MCP].x, hand_landmarks[MIDDLE_FINGER_PIP].y - hand_landmarks[MIDDLE_FINGER_MCP].y, hand_landmarks[MIDDLE_FINGER_PIP].z - hand_landmarks[MIDDLE_FINGER_MCP].z]))
    ring_tip_ring_mcp_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_TIP].x - hand_landmarks[RING_FINGER_MCP].x, hand_landmarks[RING_FINGER_TIP].y - hand_landmarks[RING_FINGER_MCP].y, hand_landmarks[RING_FINGER_TIP].z - hand_landmarks[RING_FINGER_MCP].z]))
    ring_pip_ring_mcp_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_PIP].x - hand_landmarks[RING_FINGER_MCP].x, hand_landmarks[RING_FINGER_PIP].y - hand_landmarks[RING_FINGER_MCP].y, hand_landmarks[RING_FINGER_PIP].z - hand_landmarks[RING_FINGER_MCP].z]))
    pinky_tip_pinky_mcp_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_TIP].x - hand_landmarks[PINKY_MCP].x, hand_landmarks[PINKY_TIP].y - hand_landmarks[PINKY_MCP].y, hand_landmarks[PINKY_TIP].z - hand_landmarks[PINKY_MCP].z]))
    pinky_pip_pinky_mcp_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_PIP].x - hand_landmarks[PINKY_MCP].x, hand_landmarks[PINKY_PIP].y - hand_landmarks[PINKY_MCP].y, hand_landmarks[PINKY_PIP].z - hand_landmarks[PINKY_MCP].z]))


    if (index_tip_wrist_dist < index_pip_wrist_dist and
        middle_tip_wrist_dist < middle_pip_wrist_dist and
        ring_tip_wrist_dist < ring_pip_wrist_dist and
        pinky_tip_wrist_dist < pinky_pip_wrist_dist):
        return True
    if (index_tip_index_mcp_dist < index_pip_index_mcp_dist and
        middle_tip_middle_mcp_dist < middle_pip_middle_mcp_dist and # or ??
        ring_tip_ring_mcp_dist < ring_pip_ring_mcp_dist and
        pinky_tip_pinky_mcp_dist < pinky_pip_pinky_mcp_dist):
        return True
    return False

def isOpenHand(hand_landmarks):
    index_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    index_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    middle_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    middle_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    ring_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    ring_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    pinky_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_TIP].z - hand_landmarks[WRIST].z]))
    pinky_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_PIP].z - hand_landmarks[WRIST].z]))
    
    if (index_tip_wrist_dist > index_pip_wrist_dist and
        middle_tip_wrist_dist > middle_pip_wrist_dist and
        ring_tip_wrist_dist > ring_pip_wrist_dist and
        pinky_tip_wrist_dist > pinky_pip_wrist_dist):
        return True
    return False
    
def thumbsUpAngle(hand_landmarks):
    if isFist(hand_landmarks):
        #check if angle between thumb and hand is less than 45 degrees
        thumb_vec = np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[THUMB_MCP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[THUMB_MCP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[THUMB_MCP].z])
        mcp_mcp_vec = np.array([hand_landmarks[INDEX_FINGER_MCP].x - hand_landmarks[THUMB_MCP].x, hand_landmarks[INDEX_FINGER_MCP].y - hand_landmarks[THUMB_MCP].y, hand_landmarks[INDEX_FINGER_MCP].z - hand_landmarks[THUMB_MCP].z])
        cos_theta = np.dot(thumb_vec, mcp_mcp_vec) / (np.linalg.norm(thumb_vec) * np.linalg.norm(mcp_mcp_vec))
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        theta = np.degrees(np.arccos(cos_theta))
        if theta < 45:
            return -200
        
        thumb_tip_index_mcp_vec = np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[INDEX_FINGER_MCP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[INDEX_FINGER_MCP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[INDEX_FINGER_MCP].z])
        
        height_vec = (thumb_vec + thumb_tip_index_mcp_vec) / 2
        
        thumb_tip_index_mcp_dist = np.linalg.norm(thumb_tip_index_mcp_vec)
        thumb_tip_index_pip_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[INDEX_FINGER_PIP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[INDEX_FINGER_PIP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[INDEX_FINGER_PIP].z]))
        thumb_tip_middle_pip_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[MIDDLE_FINGER_PIP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[MIDDLE_FINGER_PIP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[MIDDLE_FINGER_PIP].z]))




        #check if thumb tip is far enough from hand
        thumb_tip_thumb_mcp_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[THUMB_MCP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[THUMB_MCP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[THUMB_MCP].z]))
        thumb_cmc_wrist_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_CMC].x - hand_landmarks[WRIST].x, hand_landmarks[THUMB_CMC].y - hand_landmarks[WRIST].y, hand_landmarks[THUMB_CMC].z - hand_landmarks[WRIST].z]))
        
        if (thumb_tip_index_mcp_dist < 0.6 * thumb_tip_thumb_mcp_dist or thumb_tip_index_pip_dist <  0.6 * thumb_tip_thumb_mcp_dist or thumb_tip_middle_pip_dist <  0.6 * thumb_tip_thumb_mcp_dist
            or thumb_tip_index_pip_dist < 0.3 * thumb_cmc_wrist_dist):
            return -200
        
        thumb_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[WRIST].z]))
        thumb_ip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_IP].x - hand_landmarks[WRIST].x, hand_landmarks[THUMB_IP].y - hand_landmarks[WRIST].y, hand_landmarks[THUMB_IP].z - hand_landmarks[WRIST].z]))

        if thumb_tip_wrist_dist < thumb_ip_wrist_dist:
            return -200
        
        thumb_tip_pinky_mcp_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[PINKY_MCP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[PINKY_MCP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[PINKY_MCP].z]))
        thumb_ip_pinky_mcp_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_IP].x - hand_landmarks[PINKY_MCP].x, hand_landmarks[THUMB_IP].y - hand_landmarks[PINKY_MCP].y, hand_landmarks[THUMB_IP].z - hand_landmarks[PINKY_MCP].z]))
        if thumb_tip_pinky_mcp_dist < thumb_ip_pinky_mcp_dist:
            return -200
        
        
        height_vec2d = np.array([height_vec[0], height_vec[1]])
        cos_alpha = np.dot(height_vec2d, np.array([0, -1])) / (np.linalg.norm(height_vec2d) * 1)
        cos_alpha = np.clip(cos_alpha, -1.0, 1.0)
        alpha = np.degrees(np.arccos(cos_alpha))
        if height_vec2d[0] < 0:
            alpha = -alpha
        
        
        return alpha 

    return -200

def isMiddleFinger(hand_landmarks):
    index_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    index_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    middle_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    middle_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    ring_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    ring_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    pinky_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_TIP].z - hand_landmarks[WRIST].z]))
    pinky_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_PIP].z - hand_landmarks[WRIST].z]))

    if (index_tip_wrist_dist < index_pip_wrist_dist and
        middle_tip_wrist_dist >= middle_pip_wrist_dist and
        ring_tip_wrist_dist < ring_pip_wrist_dist and
        pinky_tip_wrist_dist < pinky_pip_wrist_dist):
        return True
    return False

def isIndexFinger(hand_landmarks):
    index_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    index_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[INDEX_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[INDEX_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    middle_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    middle_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    ring_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    ring_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    pinky_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_TIP].z - hand_landmarks[WRIST].z]))
    pinky_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_PIP].z - hand_landmarks[WRIST].z]))
    
    if (index_tip_wrist_dist >= index_pip_wrist_dist and
        middle_tip_wrist_dist < middle_pip_wrist_dist and
        ring_tip_wrist_dist < ring_pip_wrist_dist and
        pinky_tip_wrist_dist < pinky_pip_wrist_dist):
        return True
    return False

def isOk(hand_landmarks):
    middle_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    middle_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[MIDDLE_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[MIDDLE_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[MIDDLE_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    ring_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_TIP].z - hand_landmarks[WRIST].z]))
    ring_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[RING_FINGER_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[RING_FINGER_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[RING_FINGER_PIP].z - hand_landmarks[WRIST].z]))
    pinky_tip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_TIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_TIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_TIP].z - hand_landmarks[WRIST].z]))
    pinky_pip_wrist_dist = np.linalg.norm(np.array([hand_landmarks[PINKY_PIP].x - hand_landmarks[WRIST].x, hand_landmarks[PINKY_PIP].y - hand_landmarks[WRIST].y, hand_landmarks[PINKY_PIP].z - hand_landmarks[WRIST].z]))

    thumb_tip_index_tip_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_TIP].x - hand_landmarks[INDEX_FINGER_TIP].x, hand_landmarks[THUMB_TIP].y - hand_landmarks[INDEX_FINGER_TIP].y, hand_landmarks[THUMB_TIP].z - hand_landmarks[INDEX_FINGER_TIP].z]))
    thumb_mcp_index_pip_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_MCP].x - hand_landmarks[INDEX_FINGER_PIP].x, hand_landmarks[THUMB_MCP].y - hand_landmarks[INDEX_FINGER_PIP].y, hand_landmarks[THUMB_MCP].z - hand_landmarks[INDEX_FINGER_PIP].z]))
    
    thumb_mcp_thumb_ip_dist = np.linalg.norm(np.array([hand_landmarks[THUMB_MCP].x - hand_landmarks[THUMB_IP].x, hand_landmarks[THUMB_MCP].y - hand_landmarks[THUMB_IP].y, hand_landmarks[THUMB_MCP].z - hand_landmarks[THUMB_IP].z]))
    index_mcp_index_pip_dist = np.linalg.norm(np.array([hand_landmarks[INDEX_FINGER_MCP].x - hand_landmarks[INDEX_FINGER_PIP].x, hand_landmarks[INDEX_FINGER_MCP].y - hand_landmarks[INDEX_FINGER_PIP].y, hand_landmarks[INDEX_FINGER_MCP].z - hand_landmarks[INDEX_FINGER_PIP].z]))

    
    if thumb_tip_index_tip_dist < 1.7 * thumb_mcp_thumb_ip_dist or thumb_tip_index_tip_dist < 1.7 *index_mcp_index_pip_dist:
        if thumb_mcp_index_pip_dist > thumb_tip_index_tip_dist:
            if (middle_tip_wrist_dist > middle_pip_wrist_dist and
                ring_tip_wrist_dist > ring_pip_wrist_dist and
                pinky_tip_wrist_dist > pinky_pip_wrist_dist):
                return True
    return False