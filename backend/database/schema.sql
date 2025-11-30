-- Schema for User Profiles
CREATE TABLE IF NOT EXISTS user_profiles (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    background VARCHAR(50) DEFAULT 'beginner',
    preferred_language VARCHAR(10) DEFAULT 'en',
    course_progress JSONB DEFAULT '{}'::jsonb,
    last_active TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Schema for Chatbot Interaction Logs
CREATE TABLE IF NOT EXISTS chatbot_interaction_logs (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES user_profiles(user_id) ON DELETE CASCADE,
    query_text TEXT NOT NULL,
    response_text TEXT NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    feedback VARCHAR(20) -- e.g., 'helpful', 'unhelpful', 'null'
);
